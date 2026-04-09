import streamlit as st

# ---------- PAGE STATE ----------
if "users" not in st.session_state:
    st.session_state.users = {}
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------- NAVIGATION ----------
def go_home():
    st.session_state.page = "home"

def go_login():
    st.session_state.page = "login"

def go_register():
    st.session_state.page = "register"

def go_predict():
    st.session_state.page = "predict"


# ---------- HOME PAGE ----------
if st.session_state.page == "home":

    st.title("Smart Approach Monitoring with E-Pilots ✈️")
    st.write("Predicting Hard Landings for Safer Flights")

    if st.button("Login"):
        go_login()

    if st.button("Register"):
        go_register()


# ---------- LOGIN PAGE ----------
elif st.session_state.page == "login":

    st.title("Epilots Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username and password:
            if username in st.session_state.users and st.session_state.users[username] == password:
                st.success("Login Successful ✅")
                go_predict()
            else:
                st.error("User not registered or incorrect password ❌")
        else:
            st.error("Please enter username and password")

    if st.button("Back to Home"):
        go_home()


# ---------- REGISTER PAGE ----------
elif st.session_state.page == "register":

    st.title("Register")

    new_user = st.text_input("Username")
    new_pass = st.text_input("Password", type="password")

    if st.button("Register"):
        if new_user and new_pass:
            if new_user in st.session_state.users:
                st.error("User already exists ❌")
            else:
                st.session_state.users[new_user] = new_pass
                st.success("Account Created Successfully ✅")
        else:
            st.error("Please fill all fields")

    if st.button("Back to Home"):
        go_home()


# ---------- PREDICTION PAGE ----------
elif st.session_state.page == "predict":

    st.title("Flight Hard Landing Prediction")

    approach_speed = st.number_input("Approach Speed (knots)", min_value=0, max_value=180)
    altitude = st.number_input("Altitude at Threshold (feet)", min_value=0, max_value=100)
    wind_speed = st.number_input("Wind Speed (knots)", min_value=0, max_value=50)
    runway = st.selectbox("Runway Condition", ["Dry", "Wet", "Icy"])
    aircraft_weight = st.number_input("Aircraft Weight (tons)", min_value=0, max_value=500)
    pilot_experience = st.number_input("Pilot Experience (years)", min_value=0, max_value=40)

    if st.button("Predict"):

        if approach_speed == 0 or altitude == 0:
            st.warning("⚠️ Please enter all values")

        else:
            # SAME DJANGO LOGIC
            if (pilot_experience < 5 or 
                approach_speed > 150 or 
                altitude > 40 or 
                wind_speed > 20):

                result = "Yes"

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

    if st.button("Logout"):
        go_home()
