# transactions.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId
from web3 import Web3
import os
import json

router = APIRouter()

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["fentam"]
txrequests = db["txrequests"]

# Web3 and contract setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "contract_info.json")) as f:
    contract_info = json.load(f)
contract_address = contract_info["address"]

with open(os.path.join(BASE_DIR, "artifacts/contracts/FentanylSupplyChain.sol/FentanylSupplyChain.json")) as f:
    artifact = json.load(f)
    abi = artifact["abi"]

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
contract = w3.eth.contract(address=contract_address, abi=abi)
admin_account = w3.eth.accounts[0]  # Use first account as admin

# === MODELS ===
class TxRequestModel(BaseModel):
    requestedBy: str
    actionType: str
    payload: str  # ✅ Treat as raw string, not JSON object


# === ENDPOINTS ===

# Submit new tx request
@router.post("/api/tx/submit")
def submit_tx(data: TxRequestModel):
    tx = {
        "requestedBy": data.requestedBy,
        "actionType": data.actionType,
        "payload": data.payload,  # ✅ Already a string
        "approved": False
    }
    result = txrequests.insert_one(tx)
    return {"message": "Transaction submitted", "id": str(result.inserted_id)}


# Get unapproved requests
@router.get("/api/tx/pending")
def get_pending_tx():
    pending = list(txrequests.find({"approved": False}))
    for tx in pending:
        tx["_id"] = str(tx["_id"])
    return pending


# Approve and submit tx to blockchain
@router.post("/api/tx/approve/{tx_id}")
def approve_tx(tx_id: str):
    tx = txrequests.find_one({"_id": ObjectId(tx_id)})
    if not tx:
        raise HTTPException(status_code=404, detail="Transaction not found")

    try:
        # 1. First call submitRequest (to store it in mapping)
        submit_tx = contract.functions.submitRequest(
            tx["actionType"],
            tx["payload"]
        ).transact({"from": Web3.to_checksum_address(tx["requestedBy"])})

        w3.eth.wait_for_transaction_receipt(submit_tx)

        # 2. Then call approveRequest to trigger logic
        approve_tx = contract.functions.approveRequest(
            contract.functions.requestCount().call()
        ).transact({"from": admin_account})

        w3.eth.wait_for_transaction_receipt(approve_tx)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Blockchain error: {str(e)}")

    txrequests.update_one({"_id": ObjectId(tx_id)}, {"$set": {"approved": True}})
    return {"message": "Transaction approved and submitted to blockchain."}


# List all drugs on chain
@router.get("/api/tx/drugs")
def list_drugs():
    drugs = []
    count = contract.functions.drugCount().call()
    for i in range(1, count + 1):
        d = contract.functions.drugs(i).call()
        drugs.append({
            "id": d[0],
            "name": d[1],
            "manufacturer": d[2],
            "timestamp": d[3],
            "owner": d[4]  #  Use consistent key
        })
    return drugs



# Get current owner of drug
@router.get("/api/tx/owner/{drug_id}")
def get_current_owner(drug_id: int):
    try:
        drug = contract.functions.drugs(drug_id).call()
        return {
            "id": drug[0],
            "name": drug[1],
            "manufacturer": drug[2],
            "timestamp": drug[3],
            "currentOwner": drug[4]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/tx/debug")
def debug_drug_data():
    drugs = []
    count = contract.functions.drugCount().call()
    for i in range(1, count + 1):
        d = contract.functions.drugs(i).call()
        drugs.append({
            "id": d[0],
            "name": d[1],
            "manufacturer": d[2],
            "timestamp": d[3],
            "owner": d[4]  #  match above
        })
    return drugs


