
import streamlit as st
import pandas as pd
import requests

# FastAPI endpoints
GET_API_URL = "http://127.0.0.1:8000/get_s_matrix/"
POST_API_URL = "http://127.0.0.1:8000/process_s_matrix/"

# Streamlit app setup
st.set_page_config(page_title="S-Matrix to RLC Converter", layout="wide")
st.title("S-Matrix to RLC Converter")
st.markdown("""
<style>
    .stButton>button { 
        background-color: #4CAF50; 
        color: white; 
        border: none; 
        padding: 10px 20px; 
        font-size: 16px; 
        border-radius: 5px;
    }
    .stButton>button:hover { 
        background-color: #45a049; 
    }
</style>
""", unsafe_allow_html=True)

# Fetch S-matrix data
# Fetch S-matrix data
st.header("1. Fetch S-Matrix Data")
col1, col2 = st.columns(2)

if "s_matrix" not in st.session_state:
    st.session_state["s_matrix"] = None

with col1:
    if st.button("Fetch as JSON"):
        response = requests.get(GET_API_URL, params={"format": "json"})
        if response.status_code == 200:
            st.session_state["s_matrix"] = response.json()["s_matrix"]
            st.success("Data fetched successfully!")
            st.write(pd.DataFrame(st.session_state["s_matrix"], columns=["S11", "S12"]))
        else:
            st.error("Failed to fetch data.")

with col2:
    if st.button("Fetch as CSV"):
        response = requests.get(GET_API_URL, params={"format": "csv"})
        if response.status_code == 200:
            st.success("CSV downloaded. Check your downloads folder!")
            st.download_button("Download CSV", response.content, file_name="s_matrix.csv")
        else:
            st.error("Failed to fetch data.")

# Process S-matrix
if st.session_state["s_matrix"]:
    st.header("2. Process S-Matrix")
    if st.button("Calculate RLC"):
        payload = {"s_matrix": st.session_state["s_matrix"]}
        response = requests.post(POST_API_URL, json=payload)  # Ensure `json=payload` is used

        if response.status_code == 200:
            rlc_values = response.json()["rlc_values"]
            rlc_df = pd.DataFrame(rlc_values)
            st.write("RLC Results")
            st.dataframe(rlc_df)

            # Copy-to-clipboard button
            st.write("Copy Results")
            st.code(rlc_df.to_csv(index=False), language="plaintext")
            st.download_button("Copy to Clipboard", rlc_df.to_csv(index=False), file_name="rlc_results.csv")
        else:
            st.error(f"Failed to process data: {response.text}")


