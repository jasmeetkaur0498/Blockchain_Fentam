# pages/admin_dashboard.py

import streamlit as st
import requests

API_TX = "http://localhost:8000/api/tx"

st.title(" Admin Dashboard")

if "user" not in st.session_state or st.session_state["user"]["role"] != "admin":
    st.error("Unauthorized. Please log in as admin.")
    st.stop()

user = st.session_state["user"]
st.write(f"Welcome, {user['name']} ({user['role']})")

st.subheader(" Pending Drug Requests")

try:
    res = requests.get(f"{API_TX}/pending")
    if res.status_code == 200:
        pending_tx = res.json()
        if not pending_tx:
            st.info("No pending transactions.")
        else:
            for tx in pending_tx:
                with st.expander(f"Request #{tx['_id']} - {tx['actionType']}"):
                    st.code(tx["payload"], language="json")
                    if st.button("Approve", key=tx["_id"]):
                        try:
                            approve_res = requests.post(f"{API_TX}/approve/{tx['_id']}")
                            if approve_res.status_code == 200:
                                st.success("Transaction approved and submitted to blockchain.")
                                st.rerun()
                            else:
                                st.error("Approval failed.")
                        except Exception as e:
                            st.error(f"Error approving transaction: {str(e)}")
    else:
        st.error("Failed to fetch transactions.")
except Exception as e:
    st.error(f"Backend error: {e}")



