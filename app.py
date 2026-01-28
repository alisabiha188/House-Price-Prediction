import streamlit as st
import joblib
import numpy as np
import os

# ------------------------------
# Load the trained model
# ------------------------------
MODEL_FILE = "housepre_model.pkl"

if os.path.exists(MODEL_FILE):
    model = joblib.load(MODEL_FILE)
    st.success("Model loaded successfully!")
else:
    st.error(f"{MODEL_FILE} not found. Please train and save the model first.")
    st.stop()  # Stop the app if model doesn't exist

# ------------------------------
# App Title
# ------------------------------
st.title("House Price Prediction App")
st.write("Enter house details to predict the price")

# ------------------------------
# User Inputs
# ------------------------------
area = st.number_input("Area (sq ft)", min_value=0)
bedrooms = st.number_input("Bedrooms", min_value=0, step=1)
bathrooms = st.number_input("Bathrooms", min_value=0, step=1)
stories = st.number_input("Stories", min_value=0, step=1)

mainroad = st.selectbox("Main Road", ["Yes", "No"])
guestroom = st.selectbox("Guest Room", ["Yes", "No"])
basement = st.selectbox("Basement", ["Yes", "No"])
hotwaterheating = st.selectbox("Hot Water Heating", ["Yes", "No"])
airconditioning = st.selectbox("Air Conditioning", ["Yes", "No"])
prefarea = st.selectbox("Preferred Area", ["Yes", "No"])

parking = st.number_input("Parking Spaces", min_value=0, step=1)

furnishingstatus = st.selectbox(
    "Furnishing Status",
    ["Unfurnished", "Semi-Furnished", "Furnished"]
)

# ------------------------------
# Encode Inputs
# ------------------------------
binary_map = {"Yes": 1, "No": 0}
furnish_map = {
    "Unfurnished": 0,
    "Semi-Furnished": 1,
    "Furnished": 2
}

input_data = np.array([[ 
    area,
    bedrooms,
    bathrooms,
    stories,
    binary_map[mainroad],
    binary_map[guestroom],
    binary_map[basement],
    binary_map[hotwaterheating],
    binary_map[airconditioning],
    parking,
    binary_map[prefarea],
    furnish_map[furnishingstatus]
]])

# ------------------------------
# Prediction
# ------------------------------
if st.button("Predict Price"):
    try:
        prediction = model.predict(input_data)
        st.success(f"Estimated House Price: {prediction[0]:,.2f}")
    except Exception as e:
        st.error(f"Error during prediction: {e}")
