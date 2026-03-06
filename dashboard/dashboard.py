import streamlit as st
import requests

st.title("Credit Card Fraud Detection")

st.write("Enter transaction features separated by commas")

features = st.text_input("Features")

if st.button("Predict"):

    features_list = [float(x) for x in features.split(",")]

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json={"features": features_list}
    )

    result = response.json()

    st.write("Fraud Probability:", result["fraud_probability"])
    st.write("Prediction:", result["prediction"])
