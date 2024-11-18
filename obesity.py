import streamlit as st
import pandas as pd
import pickle
import numpy as np


with open("obesity_model.pkl", "rb") as f:
    model = pickle.load(f)

def user_input_features():
    age = st.number_input("Age")
    height = st.number_input("Height (m)")
    weight = st.number_input("weight (kg)")

    gender = st.selectbox("Gender", ["Male", "Female"])
    family_history = st.radio("Family history of overweight", ["Yes", "No"])

    data = {
        "Age": age,
        "Height": height,
        "Weight": weight,
        "Gende_Male": 1 if gender == "Male" else 0,  
        "family_history_with_overweight_Yes": 1 if family_history == "Yes" else 0  
    }
    features = pd.DataFrame(data, index=[0])
    return features

st.title("Obesity Level Prediction")

input_df = user_input_features()

if st.button("Predict"):
    prediction = model.predict(input_df)
    st.write("Predicted Obesity Level:", prediction[0])
