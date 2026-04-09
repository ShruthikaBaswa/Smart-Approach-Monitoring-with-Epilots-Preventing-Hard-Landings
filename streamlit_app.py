import streamlit as st

# TITLE
st.title("Smart Approach Monitoring with E-Pilots ✈️")
st.write("This project predicts hard landing risk using flight parameters.")

# INPUTS (same as your Django form)
approach_speed = st.number_input("Approach Speed (knots)", min_value=0, max_value=180)
altitude = st.number_input("Altitude at Threshold (feet)", min_value=0, max_value=100)
wind_speed = st.number_input("Wind Speed (knots)", min_value=0, max_value=50)
runway = st.selectbox("Runway Condition", ["Dry", "Wet", "Icy"])
aircraft_weight = st.number_input("Aircraft Weight (tons)", min_value=0, max_value=500)
pilot_experience = st.number_input("Pilot Experience (years)", min_value=0, max_value=40)

# BUTTON
if st.button("Predict"):

    # CHECK EMPTY INPUT
    if approach_speed == 0 or altitude == 0:
        st.warning("⚠️ Please enter all values")
    
    else:
        # SAME LOGIC AS YOUR DJANGO CODE
        if (pilot_experience < 5 or 
            approach_speed > 150 or 
            altitude > 40 or 
            wind_speed > 20):

            result = "Yes"  # Hard landing risk

        else:
            if runway == "Icy" or aircraft_weight > 200:
                result = "Yes"
            else:
                result = "No"

        # OUTPUT
        if result == "Yes":
            st.error("⚠️ Prediction: Hard Landing is YES")
        else:
            st.success("✅ Prediction: Hard Landing is NO")
