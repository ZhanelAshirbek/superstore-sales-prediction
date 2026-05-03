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
        0,   # Order ID
        0,   # Ship Mode
        0,   # Customer ID
        0,   # Customer Name
        0,   # Segment
        0,   # Country
        0,   # City
        0,   # State
        region,
        0,   # Product ID
        category,
        0,   # Sub-Category
        0,   # Product Name
        quantity,
        discount,
        profit,
        2017,
        1,
        1
    ]], columns=[
        'Order ID',
        'Ship Mode',
        'Customer ID',
        'Customer Name',
        'Segment',
        'Country',
        'City',
        'State',
        'Region',
        'Product ID',
        'Category',
        'Sub-Category',
        'Product Name',
        'Quantity',
        'Discount',
        'Profit',
        'order_year',
        'order_month',
        'order_day'
    ])

    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)

    st.success(f"Predicted Sales: ${prediction[0]:.2f}")
