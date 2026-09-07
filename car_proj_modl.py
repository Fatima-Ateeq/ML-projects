import joblib
import streamlit as st
import pandas as pd
df = pd.read_csv("cardekho_dataset.csv")

model = joblib.load("car_price_model.pkl")
m_columns = joblib.load("car_columns.pkl")


st.title("🚗 Car Prediction Price")

#user inputs
vehicle_age = st.number_input(
    "Vehicle Age",
    min_value=0,
    max_value= 50,
    value=3
)
Km_driven = st.number_input(
    "KM Driven",
    min_value=0,
    value=3000
)
mileage = st.number_input(
    "Mileage",
    min_value=0.0,
    value=20.5
)
engine = st.number_input(
    "Engine",
    min_value=500,
    value=1498
)
max_power = st.number_input(
    "Max Power",
    min_value=0.0,
    value= 110.0
)
seats = st.number_input(
    "Seats",
    min_value=2,
    max_value=10,
    value=5
)
#Select box

brand = st.selectbox(
    "Brand",
     sorted(df['brand'].unique())
        
)

model_name = st.selectbox(
    "Model",
    sorted(df["model"].unique())
)
Seller_Type = st.selectbox(
    "Seller Type",
    [
        "Dealer",
        "Individual",
        "Trustmark Dealer"
    ]
)
fuel_type = st.selectbox(
    "Fuel Type",
    [
        "CNG",
        "Diesel",
        "Electric",
        "LPG",
        "Petrol"
    ]
)
transmission_type = st.selectbox(
    "Transmission",
    [
        "Automatic",
        "Manual"
    ]
)
#prediction button
if st.button("prediction"):

  new_car = {
    "vehicle_age": vehicle_age,
    "km_driven": Km_driven,
    "mileage": mileage,
    "engine": engine,
    "max_power": max_power,
    "seats": seats,
    "brand": brand,
    "model": model_name,
    "seller_type": Seller_Type,
    "fuel_type": fuel_type,
    "transmission_type": transmission_type
  }

  df_new = pd.DataFrame([new_car])

#one hot encoding
#df_new = pd.DataFrame([new_car]) why new car close in [] and second think is one hot encdonf just work on categrical columns not int
  df_new = pd.get_dummies(df_new, dtype= int)


# Match training columns
  new_car_df = df_new.reindex(
        columns=m_columns,
        fill_value=0
    )

    # Prediction
  prediction = model.predict(new_car_df)

  st.success(
        f"💰 Predicted Selling Price: ₹{prediction[0]:,.0f}"
    )