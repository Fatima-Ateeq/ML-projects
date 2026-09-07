import joblib
import streamlit as st
import pandas as pd
df = pd.read_csv("cardekho_dataset.csv")

model = joblib.load("car_price_model.pkl")
m_columns = joblib.load("car_columns.pkl")

st.set_page_config(

    page_title="Selling Price App",
    layout="wide"

)

st.markdown("""
<style>

.block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
}


.price_card{
background: white;
pading:25px;
border-radius: 15px;
border:1px solid #e5e7eb;
text-align: center
}
.price_card h1{
color: #079447;
font-size: 42px;
}
.exact-price{
background: #ecfdf3;
color: #07833f;
padding: 12px;
border-radius: 8px;
font-weight: bold;

}
.spn{
color: #079447;
}


</style>
""", unsafe_allow_html=True)


st.title("🚗 Car Selling Price Predictor")
co1, co2 = st.columns(2)
#user inputs

with co1:
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
with co2:
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
  pred_price = prediction[0]

  #convert to lakh
  price_lakh = pred_price/100000

  st.success(
        f"💰 Predicted Selling Price: ₹{pred_price:,.0f}"
    )
  
  #ccol1, ccol2 = st.columns([1,1.5])
  #Left Price Card
  #with ccol1:
  st.markdown(f"""
     <div class="price_card">
     <h4>💰 Estimated Selling Price</h4>
     <h1>₹{price_lakh:.2f} Lakh</h1>
     <div class="exact-price">
         ₹{pred_price:,.0f} &nbsp; (Exact Price)
     </div>
     <p>Based on the vehicle details provided, the model estimates
       the selling price at approximately ₹{price_lakh:.2f} lakh.</p>
     </div>
    """,unsafe_allow_html= True)
  # RIGHT CARD - Entered Vehicle Details

  

with st.sidebar:
#   st.markdown("## 🚗 Car Price Prdictor")
#   st.caption("Machine Learning powered vehicle Price estimator")
  
  st.markdown("""
   <h2> 🤖 Model Information</h2>
  """, unsafe_allow_html=True)
  st.markdown("""
  <p>
  <strong>Model: </strong>
  <span class="spn"><b>Random Forest Regressor</b></span>
  </p>
  """,unsafe_allow_html= True)
  st.metric(
    label = "📊 Model R²",
    value= "92.67%"
  )
  st.metric(
        label="💰 MAE",
        value="₹103K"
    )
  st.metric(
    label="📈 RMSE",
    value="₹233K"
  )
  st.metric(
        label="🔢 Features Used",
        value="168"
    )

  st.divider()

  st.markdown("### 💡 How it works")
  st.markdown("""
    **1.** 🚗 Enter Vehicle detials<br>
    **2.** 🔄 Data is Preprocessed<br>
    **3.** 🔢 Catgorical data is encoded<br>
    **4.** 🤖 Random Forest Analyze the data<br>
    **5.** 💰 Estimated Selling price is Generated<br>
""",unsafe_allow_html=True)
