# pages/manufacturer.py
import streamlit as st
import requests

API_TX = "http://localhost:8000/api/tx"

st.title(" Manufacturer Dashboard")

if "user" not in st.session_state:
    st.error("Please login first.")
    st.stop()

user = st.session_state["user"]
st.write(f"Welcome, {user['name']} ({user['role']})")

# --- Create Drug Request ---
st.subheader(" Submit Drug Creation Request")
drug_name = st.text_input("Drug Name")

if st.button("Submit Request"):
    if not drug_name:
        st.warning("Please enter a drug name.")
    else:
        res = requests.post(f"{API_TX}/submit", json={
            "actionType": "createDrug",
            "payload": drug_name,  #  Just the name string
            "requestedBy": user["walletAddress"]
        })
        if res.status_code == 200:
            st.success("Drug creation request submitted!")
        else:
            st.error("Submission failed.")


# --- Transfer Drug ---
st.subheader(" Transfer Drug to Distributor")

drug_id = st.text_input("Drug ID to Transfer")
new_owner = st.text_input("Distributor Wallet Address")

if st.button("Transfer Drug"):
    if not drug_id or not new_owner:
        st.warning("Please fill both fields.")
    else:
        transfer_payload = f"{drug_id.strip()},{new_owner.strip()}"  #  Comma-separated string
        res = requests.post(f"{API_TX}/submit", json={
            "actionType": "transfer",
            "payload": transfer_payload,
            "requestedBy": user["walletAddress"]
        })
        if res.status_code == 200:
            st.success("Transfer request submitted!")
        else:
            st.error("Transfer submission failed.")



