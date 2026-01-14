import streamlit as st
from web3_helpers import users_collection

st.title("📋 Register as a Network Entity")

name = st.text_input("Name")
role = st.selectbox("Role", ["Manufacturer", "Distributor", "Pharmacy", "Regulator"])
address = st.text_input("Wallet Address (0x...)")

if st.button("Submit Registration"):
    if not name or not address:
        st.error("Please fill all fields.")
    else:
        # Check if user exists
        if users_collection.find_one({"address": address}):
            st.warning("This wallet is already registered.")
        else:
            users_collection.insert_one({
                "name": name,
                "role": role,
                "address": address,
                "approved": False
            })
            st.success("Registration submitted! Awaiting admin approval.")
