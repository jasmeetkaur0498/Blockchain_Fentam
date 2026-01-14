# pages/pharmacy.py
import streamlit as st
import requests

API_TX = "http://localhost:8000/api/tx"

st.title(" Pharmacy Dashboard")

if "user" not in st.session_state:
    st.error("Please login first.")
    st.stop()

user = st.session_state["user"]
wallet = user.get("walletAddress")

st.write(f"Welcome, {user['name']} ({user['role']})")

if not wallet:
    st.error(" Your wallet address is missing. Please contact admin.")
    st.stop()

st.subheader(" Received Drugs")

try:
    res = requests.get(f"{API_TX}/drugs")
    if res.status_code == 200:
        all_drugs = res.json()

        # Filter by current owner
        received = [d for d in all_drugs if d["owner"].lower() == wallet.lower()]
        if received:
            for d in received:
                st.markdown(f"""
                - **ID**: {d['id']}
                - **Name**: {d['name']}
                - **Manufacturer**: {d['manufacturer']}
                - **Owner**: `{d['owner']}`
                """)
        else:
            st.info("No drugs received yet.")
    else:
        st.error(" Failed to fetch drug data from backend.")
except Exception as e:
    st.error(f" Error: {e}")


