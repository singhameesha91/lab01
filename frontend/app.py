import streamlit as st
import requests
import os

BACKEND_URL = os.getenv("BACKEND_URL", "http://backend:8000")

st.title("Frontend Microservice")

if st.button("Get Message from Backend"):
    try:
        response = requests.get(f"{BACKEND_URL}/message")
        data = response.json()
        st.success(data["message"])
    except Exception as e:
        st.error(f"Error calling backend: {e}")
