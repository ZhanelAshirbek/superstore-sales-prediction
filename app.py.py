import streamlit as st
import pandas as pd
import joblib

# load model
model = joblib.load('sales_model.pkl')
scaler = joblib.load('scaler.pkl')

st.title("Superstore Sales Prediction")

st.write("Enter values to predict sales")

category = st.number_input("Category (0-2)", min_value=0, max_value=2, value=0)
region = st.number_input("Region (0-3)", min_value=0, max_value=3, value=0)
quantity = st.number_input("Quantity", min_value=1, value=1)
discount = st.number_input("Discount", min_value=0.0, max_value=1.0, value=0.0)
profit = st.number_input("Profit", value=0.0)

if st.button("Predict Sales"):

    input_data = pd.DataFrame([[
        0,         # Ship Mode
        0,         # Segment
        0,         # Country
        0,         # City
        0,         # State
        region,
        category,
        0,         # Sub-Category
        quantity,
        discount,
        profit,
        2017,      # order_year
        1,         # order_month
        1          # order_day
    ]])

    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)

    st.success(f"Predicted Sales: ${prediction[0]:.2f}")
