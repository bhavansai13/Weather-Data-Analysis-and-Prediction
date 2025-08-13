import streamlit as st
from utils import predict_weather_and_temp

st.title("⛅ Weather Prediction App")
st.write("Enter a date and get the predicted temperature & weather.")

# Date input
date_input = st.date_input("Select a date")

if st.button("Predict"):
    try:
        temp, weather = predict_weather_and_temp(str(date_input))
        st.success(f"📅 Date: {date_input}")
        st.info(f"🌡 Temperature: {temp:.2f}°C")
        st.info(f"☁ Weather: {weather}")
    except Exception as e:
        st.error(f"Error: {e}")




