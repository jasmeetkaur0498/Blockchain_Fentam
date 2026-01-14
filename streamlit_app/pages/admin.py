import streamlit as st
import requests

API_BASE = "http://localhost:8000/api/auth"

st.set_page_config(page_title="Admin Panel", layout="centered")
st.title("🔐 Admin Approval Panel")

# Load pending users
def load_pending_users():
    try:
        res = requests.get(f"{API_BASE}/pending")
        if res.status_code == 200:
            return res.json()
        else:
            st.error(" Failed to load users.")
            return []
    except Exception as e:
        st.error(" Backend not reachable.")
        return []

users = load_pending_users()

if users:
    st.subheader(" Pending Users")
    for user in users:
        name = user.get("name", "Unknown")
        role = user.get("role", "N/A")
        email = user.get("email", "No Email")
        user_id = user.get("_id")

        with st.expander(f"{name} ({role}) - {email}"):
            st.write(f" Email: {email}")
            st.write(f" Role: {role}")
            if st.button(" Approve", key=str(user_id)):
                try:
                    res = requests.post(f"{API_BASE}/approve/{user_id}")
                    if res.status_code == 200:
                        st.success(f"{name} approved!")
                        st.rerun()  #  replaced deprecated experimental_rerun()
                    else:
                        st.error(" Approval failed.")
                except Exception as e:
                    st.error(f" Could not reach backend: {e}")
else:
    st.info("ℹ️ No pending users right now.")


