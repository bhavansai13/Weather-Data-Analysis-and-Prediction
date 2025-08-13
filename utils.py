import pandas as pd
import joblib

# Load both models
temp_model = joblib.load("model/temp_model1.joblib")
weather_model = joblib.load("model/weather_model1.joblib")
label_encoder = joblib.load("model/label_encoder1.joblib")  # For decoding weather

def prepare_features(date_str):
    date = pd.to_datetime(date_str)
    return pd.DataFrame({
        "year": [date.year],
        "month": [date.month],
        "day_of_year": [date.timetuple().tm_yday]
    })

def predict_weather_and_temp(date_str):
    features = prepare_features(date_str)

    # Predict temperature
    temp_pred = temp_model.predict(features)[0]

    # Predict weather using predicted temperature
    features_with_temp = features.copy()
    features_with_temp["temp_max"] = temp_pred
    weather_pred_encoded = weather_model.predict(features_with_temp)[0]
    weather_pred = label_encoder.inverse_transform([weather_pred_encoded])[0]

    return temp_pred, weather_pred


