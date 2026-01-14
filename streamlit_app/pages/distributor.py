# distributor.py
import streamlit as st
import requests
import json

API_TX = "http://localhost:8000/api/tx"

st.title(" Distributor Dashboard")

if "user" not in st.session_state:
    st.error("Please login first.")
    st.stop()

user = st.session_state["user"]
st.write(f"Welcome, {user['name']} ({user['role']})")

if "walletAddress" not in user or not user["walletAddress"]:
    st.error("Your wallet address is missing. Please contact admin.")
    st.stop()

# --- Transfer form ---
st.subheader(" Transfer Drug to Retailer")

drug_id = st.text_input("Drug ID to Transfer")
to_address = st.text_input("Retailer Wallet Address")  #  define it here

if st.button("Transfer Drug"):
    # Convert drugId to string to safely concatenate
    payload = f"{drug_id.strip()},{to_address.strip()}"

    res = requests.post(f"{API_TX}/submit", json={
        "actionType": "transfer",
        "payload": payload,  #  plain string payload, not JSON
        "requestedBy": user["walletAddress"]
    })

    if res.status_code == 200:
        st.success("Transfer request submitted!")
    else:
        st.error("Transfer failed.")


