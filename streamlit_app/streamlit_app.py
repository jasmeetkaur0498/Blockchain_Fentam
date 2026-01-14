# streamlit_app.py
import streamlit as st
import requests
from web3_helpers import is_connected

API_BASE = "http://localhost:8000/api/auth"

st.set_page_config(page_title="Fentanyl SCM", layout="centered")

st.title("Fentanyl Supply Chain Login")
st.markdown("Built with Hardhat, MongoDB & Streamlit")

# --- Web3 Check ---
if not is_connected():
    st.error("Web3 not connected! Make sure Hardhat node is running.")
    st.stop()

# --- Tabs ---
tab1, tab2 = st.tabs(["Login", "Signup"])

# --- Login Tab ---
with tab1:
    st.subheader("Login")
    email = st.text_input("Email", key="login_email")

    if st.button("Login"):
        if not email:
            st.warning("Please enter your email.")
        else:
            try:
                res = requests.post(f"{API_BASE}/login", json={"email": email})
                if res.status_code == 200:
                    user = res.json()
                    st.session_state["user"] = user
                    st.success(f"Welcome back, {user.get('name', 'User')} ({user.get('role', '-')})!")

                    # 🔁 Switch to role page inside /pages
                    st.switch_page(f"pages/{user['role']}.py")

                else:
                    st.error(res.json().get("message", "Login failed."))
            except Exception as e:
                st.error(f"Could not reach backend: {e}")

# --- Signup Tab ---
with tab2:
    st.subheader("Signup")
    name = st.text_input("Name")
    signup_email = st.text_input("Email", key="signup_email")
    role = st.selectbox("Role", ["manufacturer", "distributor", "retailer", "pharmacy"])

    if st.button("Signup"):
        if not name or not signup_email:
            st.warning("All fields are required.")
        else:
            try:
                res = requests.post(f"{API_BASE}/signup", json={
                    "name": name,
                    "email": signup_email,
                    "role": role,
                    "walletAddress": ""
                })
                if res.status_code == 200:
                    st.success("Signup submitted. Awaiting admin approval.")
                else:
                    st.error(res.json().get("message", "Signup failed."))
            except Exception as e:
                st.error(f"Could not reach backend: {e}")

if "user" in st.session_state:
    role = st.session_state["user"]["role"]
    if role == "manufacturer":
        st.switch_page("pages/manufacturer.py")
    elif role == "distributor":
        st.switch_page("pages/distributor.py")
    elif role == "retailer":
        st.switch_page("pages/retailer.py")
    elif role == "pharmacy":
        st.switch_page("pages/pharmacy.py")


