import os
import json
from web3 import Web3
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env (optional but recommended)
load_dotenv()

# Base path to resolve relative files correctly regardless of where script runs from
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load contract address from contract_info.json
CONTRACT_INFO_PATH = os.path.join(BASE_DIR, "contract_info.json")
with open(CONTRACT_INFO_PATH, "r") as f:
    contract_data = json.load(f)
    contract_address = contract_data["address"]

# Load ABI from compiled artifacts
ABI_PATH = os.path.join(BASE_DIR, "..", "artifacts", "contracts", "FentanylSupplyChain.sol", "FentanylSupplyChain.json")
with open(ABI_PATH, "r") as f:
    artifact = json.load(f)
    abi = artifact["abi"]

# Connect to local Hardhat blockchain node
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

# Instantiate contract instance
contract = w3.eth.contract(address=contract_address, abi=abi)

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
mongo_client = MongoClient(MONGO_URI)
mongo_db = mongo_client["fentam"]
users_collection = mongo_db["users"]
txrequests_collection = mongo_db["txrequests"]

# Utility to check if blockchain is connected
def is_connected():
    return w3.is_connected()

# Blockchain execution functions (dummy logic for now)
def log_ship_transaction(drug_id, destination):
    tx = contract.functions.shipDrug(drug_id, destination).transact({'from': w3.eth.accounts[0]})
    receipt = w3.eth.wait_for_transaction_receipt(tx)
    return receipt.transactionHash.hex()

def log_receive_transaction(drug_id):
    tx = contract.functions.receiveDrug(drug_id).transact({'from': w3.eth.accounts[0]})
    receipt = w3.eth.wait_for_transaction_receipt(tx)
    return receipt.transactionHash.hex()

def log_dispense_transaction(drug_id, patient):
    tx = contract.functions.dispenseDrug(drug_id, patient).transact({'from': w3.eth.accounts[0]})
    receipt = w3.eth.wait_for_transaction_receipt(tx)
    return receipt.transactionHash.hex()





