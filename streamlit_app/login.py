import streamlit as st
from web3_helpers import users_collection

st.title("🔐 Login")

wallet = st.text_input("Enter your wallet address")

if st.button("Login"):
    user = users_collection.find_one({"address": wallet})
    if not user:
        st.error("User not registered.")
    elif not user["approved"]:
        st.warning("Waiting for admin approval.")
    else:
        st.session_state["user"] = {
            "name": user["name"],
            "email": user["email"],
            "role": user["role"],
            "address": user["address"]  # ✅ add this
        }
        st.success(f"Welcome {user['name']}! Redirecting...")
        st.experimental_rerun()
