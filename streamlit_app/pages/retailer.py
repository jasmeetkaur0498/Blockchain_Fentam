# pages/retailer.py
import streamlit as st
import requests

API_TX = "http://localhost:8000/api/tx"

st.title(" Retailer Dashboard")

if "user" not in st.session_state:
    st.error("Please login first.")
    st.stop()

user = st.session_state["user"]
st.write(f"Welcome, {user['name']} ({user['role']})")

st.subheader(" Transfer Drug to Pharmacy")

drug_id = st.text_input("Drug ID to Transfer")
new_owner = st.text_input("Pharmacy Wallet Address")

if st.button("Transfer Drug"):
    if not drug_id or not new_owner:
        st.warning("Please provide both Drug ID and Pharmacy Wallet Address.")
    else:
        payload = f"{drug_id.strip()},{new_owner.strip()}"  #  formatted string
        res = requests.post(f"{API_TX}/submit", json={
            "actionType": "transfer",
            "payload": payload,
            "requestedBy": user["walletAddress"]
        })
        if res.status_code == 200:
            st.success("Transfer request submitted!")
        else:
            st.error("Transfer submission failed.")


