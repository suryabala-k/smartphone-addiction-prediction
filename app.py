import streamlit as st
import pandas as pd
import pickle

st.set_page_config(
    page_title="Smartphone Addiction Prediction",
    page_icon="📱",
    layout="centered"
)

@st.cache_resource
def load_model():
    with open("smartphone_addiction_model.pkl", "rb") as file:
        return pickle.load(file)

try:
    model = load_model()
except Exception as error:
    st.error("Could not load the model. Please check the model file.")
    st.code(str(error))
    st.stop()

st.title("📱 Smartphone Addiction Prediction")
st.write(
    "Enter smartphone usage details to predict "
    "the project-defined addiction category."
)

st.info(
    "This is an educational project, not a medical diagnosis."
)

st.header("Student Information")

age = st.number_input(
    "Age", min_value=10, max_value=100, value=18
)

gender = st.selectbox(
    "Gender", ["Male", "Female", "Other"]
)

st.header("Smartphone Usage")

daily_usage = st.number_input(
    "Daily smartphone usage (hours)",
    min_value=0.0, max_value=24.0, value=5.0
)

sleep_hours = st.number_input(
    "Sleep duration (hours)",
    min_value=0.0, max_value=24.0, value=7.0
)

academic_performance = st.number_input(
    "Academic performance",
    min_value=0.0, max_value=100.0, value=75.0
)

phone_checks = st.number_input(
    "Phone checks per day",
    min_value=0, max_value=1000, value=50
)

apps_used = st.number_input(
    "Apps used daily",
    min_value=0, max_value=500, value=10
)

social_media = st.number_input(
    "Social media usage (hours)",
    min_value=0.0, max_value=24.0, value=2.0
)

gaming = st.number_input(
    "Gaming time (hours)",
    min_value=0.0, max_value=24.0, value=1.0
)

if st.button("Predict Addiction Category"):

    input_data = pd.DataFrame([{
        "Age": age,
        "Gender": gender,
        "Daily_Usage_Hours": daily_usage,
        "Sleep_Hours": sleep_hours,
        "Academic_Performance": academic_performance,
        "Phone_Checks_Per_Day": phone_checks,
        "Apps_Used_Daily": apps_used,
        "Time_on_Social_Media": social_media,
        "Time_on_Gaming": gaming
    }])

    try:
        prediction = model.predict(input_data)[0]

        st.subheader("Prediction Result")

        if prediction == "Low":
            st.success("Predicted Category: LOW")
        elif prediction == "Moderate":
            st.warning("Predicted Category: MODERATE")
        else:
            st.error("Predicted Category: HIGH")

        st.caption(
            "Categories are project-defined and are not "
            "medically validated thresholds."
        )

    except Exception as error:
        st.error("Prediction failed.")
        st.code(str(error))

with st.expander("About the Project"):
    st.write("""
    Smartphone Addiction Analysis Among Students

    Machine learning models evaluated:
    - Logistic Regression
    - Decision Tree
    - Random Forest
    """)
