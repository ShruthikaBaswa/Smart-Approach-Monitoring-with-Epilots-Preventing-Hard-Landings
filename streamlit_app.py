import streamlit as st

# ---------- PAGE STATE ----------
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------- CUSTOM STYLE ----------
st.markdown("""
<style>
body {
    background-color: #f0f2f6;
}
.box {
    background-color: rgba(255,255,255,0.9);
    padding: 30px;
    border-radius: 10px;
    text-align: center;
    margin-top: 100px;
}
.btn {
    margin: 10px;
}
</style>
""", unsafe_allow_html=True)

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

    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown("<h2>Smart approach monitoring with Epilots: Preventing Hard Landing</h2>", unsafe_allow_html=True)

    if st.button("Login"):
        go_login()

    if st.button("Register"):
        go_register()

    st.markdown('</div>', unsafe_allow_html=True)


# ---------- LOGIN PAGE ----------
elif st.session_state.page == "login":

    st.title("Epilots Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username and password:
            st.success("Login successful")
            go_predict()
        else:
            st.error("Invalid username or password")

    if st.button("Home"):
        go_home()


# ---------- REGISTER PAGE ----------
elif st.session_state.page == "register":

    st.title("Registration Page")

    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Register"):
        if user and pwd:
            st.success("Account created successfully")
        else:
            st.error("Fill all details")

    if st.button("Home"):
        go_home()


# ---------- PREDICTION PAGE ----------
elif st.session_state.page == "predict":

    st.markdown("<h2 style='text-align:center;'>Flight Hard Landing Prediction</h2>", unsafe_allow_html=True)

    approach_speed = st.number_input("Approach Speed (knots)", min_value=0, max_value=180)
    altitude = st.number_input("Altitude at Threshold (feet)", min_value=0, max_value=100)
    wind_speed = st.number_input("Wind Speed (knots)", min_value=0, max_value=50)
    runway = st.selectbox("Runway Condition", ["Dry", "Wet", "Icy"])
    aircraft_weight = st.number_input("Aircraft Weight (tons)", min_value=0, max_value=500)
    pilot_experience = st.number_input("Pilot Experience (years)", min_value=0, max_value=40)

    if st.button("Predict"):

        if approach_speed == 0 or altitude == 0:
            st.warning("Enter all values")
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

            st.markdown(f"""
            <div style="background-color:#d1ecf1;padding:15px;border-radius:5px;">
            <b>Prediction: Hard Landing is {result}</b>
            </div>
            """, unsafe_allow_html=True)

    if st.button("Logout"):
        go_home()

            if result == "Yes":
                st.error("⚠️ Prediction: Hard Landing is YES")
            else:
                st.success("✅ Prediction: Hard Landing is NO")

    st.button("Logout", on_click=go_home)
