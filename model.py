import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("Test Model")

tenure = st.slider("Tenure", 0, 72, 10)
monthly = st.slider("Monthly", 0, 150, 50)
total = st.slider("Total", 0, 10000, 1000)

if st.button("Predict"):
    pred = model.predict([[tenure, monthly, total]])
    st.write(pred)