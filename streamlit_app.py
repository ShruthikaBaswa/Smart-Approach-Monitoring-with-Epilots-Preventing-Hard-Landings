import streamlit as st

st.title("Smart Approach Monitoring with E-Pilots ✈️")

st.write("This project predicts hard landing risk using flight data.")

# Dummy input
speed = st.number_input("Approach Speed")
vertical_speed = st.number_input("Vertical Speed")

if st.button("Predict"):
    st.success("Safe Landing ✅ (Demo Output)")
