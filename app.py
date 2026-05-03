
import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

model = joblib.load('model.pkl')

df = pd.read_csv('Sample - Superstore.csv', encoding='latin1')
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['order_year'] = df['Order Date'].dt.year
df['order_month'] = df['Order Date'].dt.month

st.title("Superstore Sales Prediction")

ship_mode = st.selectbox("Ship Mode", df['Ship Mode'].unique())
segment = st.selectbox("Segment", df['Segment'].unique())
region = st.selectbox("Region", df['Region'].unique())
category = st.selectbox("Category", df['Category'].unique())
sub_category = st.selectbox("Sub-Category", df['Sub-Category'].unique())

quantity = st.slider("Quantity", 1, 14, 1)
discount = st.slider("Discount", 0.0, 1.0, 0.0)

year = st.selectbox("Year", sorted(df['order_year'].unique()))
month = st.slider("Month", 1, 12, 1)

if st.button("Predict Sales"):
    input_df = pd.DataFrame([{
        'Ship Mode': ship_mode,
        'Segment': segment,
        'Region': region,
        'Category': category,
        'Sub-Category': sub_category,
        'Quantity': quantity,
        'Discount': discount,
        'order_year': year,
        'order_month': month
    }])

    pred = model.predict(input_df)
    st.success(f"Predicted Sales: ${pred[0]:.2f}")

st.subheader("Sales Distribution")
fig, ax = plt.subplots()
ax.hist(df['Sales'], bins=30)
st.pyplot(fig)

df = pd.read_csv("Sample - Superstore.csv", encoding='latin1')

st.subheader("Sales Distribution")

fig, ax = plt.subplots()
ax.hist(df['Sales'], bins=30)
st.pyplot(fig)

st.subheader("Sales by Category")

fig, ax = plt.subplots()
sns.barplot(data=df, x='Category', y='Sales', ax=ax)
st.pyplot(fig)

st.subheader("Sales by Region")

fig, ax = plt.subplots()
sns.barplot(data=df, x='Region', y='Sales', ax=ax)
st.pyplot(fig)
