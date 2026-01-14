from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId
import os

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["fentam"]
users = db["users"]

# FastAPI app setup
app = FastAPI()

# CORS config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class SignupRequest(BaseModel):
    name: str
    email: str
    role: str
    walletAddress: str

class LoginRequest(BaseModel):
    email: str

# Routes
@app.post("/api/auth/signup")
def signup(data: SignupRequest):
    if users.find_one({"email": data.email}):
        raise HTTPException(status_code=400, detail="User already exists.")

    users.insert_one({
        "name": data.name,
        "email": data.email,
        "role": data.role,
        "address": data.walletAddress,  # ✅ Make sure this is coming from frontend
        "approved": False
    })
    return {"message": "Signup successful. Awaiting admin approval."}

@app.post("/api/auth/login")
def login(data: LoginRequest):
    user = users.find_one({"email": data.email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    if not user.get("approved"):
        raise HTTPException(status_code=403, detail="User not approved.")
    user["_id"] = str(user["_id"])
    return user

@app.get("/api/auth/pending")
def get_pending_users():
    pending = list(users.find({"approved": False}))
    for user in pending:
        user["_id"] = str(user["_id"])
    return pending

@app.post("/api/auth/approve/{user_id}")
def approve_user(user_id: str):
    result = users.update_one({"_id": ObjectId(user_id)}, {"$set": {"approved": True}})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found.")
    return {"message": "User approved."}

# ✅ Mount transaction API
from transactions import router as tx_router
app.include_router(tx_router)

