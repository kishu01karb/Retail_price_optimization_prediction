import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title="Retail Price Prediction", layout="wide")

st.title("🛒 Retail Price Prediction App")
st.markdown("Predict optimal product prices using Machine Learning (XGBoost)")

# Load trained model
model = joblib.load("xgb_price_model.pkl")

# Load feature names
feature_columns = joblib.load("feature_columns.pkl")

st.sidebar.header("📥 Enter Product Details")

def user_inputs():
    qty = st.sidebar.number_input("Quantity", 1, 1000, 10)
    freight_price = st.sidebar.number_input("Freight Price", 0.0, 100.0, 15.0)
    product_score = st.sidebar.slider("Product Score", 1.0, 5.0, 4.5)
    comp_1 = st.sidebar.number_input("Competitor 1 Price", 0.0, 500.0, 105.0)
    comp_2 = st.sidebar.number_input("Competitor 2 Price", 0.0, 500.0, 110.0)
    comp_3 = st.sidebar.number_input("Competitor 3 Price", 0.0, 500.0, 108.0)
    lag_price = st.sidebar.number_input("Last Month Price", 0.0, 500.0, 102.0)

    data = {
        'qty': qty,
        'freight_price': freight_price,
        'product_score': product_score,
        'comp_1': comp_1,
        'comp_2': comp_2,
        'comp_3': comp_3,
        'lag_price': lag_price
    }
    return data

input_data = user_inputs()

if st.button("🔮 Predict Price"):
    df_input = pd.DataFrame([input_data])
    df_input = df_input.reindex(columns=feature_columns, fill_value=0)

    prediction = model.predict(df_input)[0]

    st.success(f"💰 Predicted Optimal Price: ${prediction:.2f}")

