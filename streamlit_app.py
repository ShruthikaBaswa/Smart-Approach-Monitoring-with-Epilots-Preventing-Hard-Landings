import streamlit as st
import time

st.title("AI-Based Smart Approach Monitoring System ✈️")

st.write("Predicts hard landing risk using flight parameters.")

# Inputs
speed = st.number_input("Approach Speed (knots)", min_value=0, max_value=180, value=120)
altitude = st.number_input("Altitude at Threshold (feet)", min_value=0, max_value=100, value=80)
wind_speed = st.number_input("Wind Speed (knots)", min_value=0, max_value=50, value=10)
runway = st.selectbox("Runway Condition", ["Dry", "Wet", "Snow"])
weight = st.number_input("Aircraft Weight (tons)", min_value=0, max_value=500, value=200)
experience = st.number_input("Pilot Experience (years)", min_value=0, max_value=40, value=5)

if st.button("Predict"):

    with st.spinner("Analyzing flight data..."):
        time.sleep(2)

    # Risk score system (REALISTIC LOGIC)
    risk_score = 0

    if speed > 150:
        risk_score += 2
    if altitude < 50:
        risk_score += 2
    if wind_speed > 30:
        risk_score += 2
    if runway == "Wet":
        risk_score += 1
    if runway == "Snow":
        risk_score += 2
    if weight > 300:
        risk_score += 1
    if experience < 5:
        risk_score += 2

    # FINAL DECISION
    if risk_score >= 5:
        st.error("⚠️ YES - Hard Landing Risk")
    else:
        st.success("✅ NO - Safe Landing")

    # Show score
    st.info(f"Risk Score: {risk_score}")
