import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set Streamlit page configuration
st.set_page_config(
    page_title="Multiple Disease Prediction System",
    page_icon="🩺",
    layout="centered"
)

# Load the saved models
diabetes_model = pickle.load(open("diabetes_model.sav", "rb"))
heart_disease_model = pickle.load(open("heart_disease_model.sav", "rb"))
parkinsons_model = pickle.load(open("parkinsons_model.sav", "rb"))

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        "Multiple Disease Prediction System",
        ["Diabetes Prediction", "Heart Disease Prediction", "Parkinson's Prediction"],
        icons=["activity", "heart", "person"],
        default_index=0
    )

# Diabetes Prediction Page
if selected == "Diabetes Prediction":
    st.title("Diabetes Prediction")

    # Input fields
    Pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=20)
    Glucose = st.number_input('Glucose Level', min_value=0)
    BloodPressure = st.number_input('Blood Pressure value', min_value=0)
    SkinThickness = st.number_input('Skin Thickness value', min_value=0)
    Insulin = st.number_input('Insulin Level', min_value=0)
    BMI = st.number_input('BMI value', min_value=0.0, format="%.2f")
    DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', min_value=0.0, format="%.3f")
    Age = st.number_input('Age of the Person', min_value=1)

    # Prediction
    if st.button("Diabetes Test Result"):
        diabetes_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if diabetes_prediction[0] == 1:
            st.error("The person is Diabetic")
        else:
            st.success("The person is Non-Diabetic")

# Heart Disease Prediction Page
if selected == "Heart Disease Prediction":
    st.title("Heart Disease Prediction")

    # Input fields
    age = st.number_input("Age", min_value=1)
    sex = st.number_input("Sex (1 = male; 0 = female)", min_value=0, max_value=1)
    cp = st.number_input("Chest Pain types (0-3)", min_value=0, max_value=3)
    trestbps = st.number_input("Resting Blood Pressure", min_value=0)
    chol = st.number_input("Serum Cholestoral in mg/dl", min_value=0)
    fbs = st.number_input("Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)", min_value=0, max_value=1)
    restecg = st.number_input("Resting Electrocardiographic results (0-2)", min_value=0, max_value=2)
    thalach = st.number_input("Maximum Heart Rate achieved", min_value=0)
    exang = st.number_input("Exercise Induced Angina (1 = yes; 0 = no)", min_value=0, max_value=1)
    oldpeak = st.number_input("ST depression induced by exercise", format="%.1f")
    slope = st.number_input("Slope of the peak exercise ST segment (0-2)", min_value=0, max_value=2)
    ca = st.number_input("Major vessels colored by flourosopy (0-4)", min_value=0, max_value=4)
    thal = st.number_input("Thal (0 = normal; 1 = fixed defect; 2 = reversible defect)", min_value=0, max_value=2)

    if st.button("Heart Disease Test Result"):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,
                                                          thalach, exang, oldpeak, slope, ca, thal]])
        if heart_prediction[0] == 1:
            st.error("The person has Heart Disease")
        else:
            st.success("The person does not have Heart Disease")

# Parkinson's Prediction Page
if selected == "Parkinson's Prediction":
    st.title("Parkinson's Disease Prediction")

    # Input fields
    fo = st.number_input("MDVP:Fo(Hz)", format="%.2f")
    fhi = st.number_input("MDVP:Fhi(Hz)", format="%.2f")
    flo = st.number_input("MDVP:Flo(Hz)", format="%.2f")
    jitter_percent = st.number_input("MDVP:Jitter(%)", format="%.5f")
    jitter_abs = st.number_input("MDVP:Jitter(Abs)", format="%.5f")
    rap = st.number_input("MDVP:RAP", format="%.5f")
    ppq = st.number_input("MDVP:PPQ", format="%.5f")
    ddp = st.number_input("Jitter:DDP", format="%.5f")
    shimmer = st.number_input("MDVP:Shimmer", format="%.5f")
    shimmer_db = st.number_input("MDVP:Shimmer(dB)", format="%.5f")
    apq3 = st.number_input("Shimmer:APQ3", format="%.5f")
    apq5 = st.number_input("Shimmer:APQ5", format="%.5f")
    apq = st.number_input("MDVP:APQ", format="%.5f")
    dda = st.number_input("Shimmer:DDA", format="%.5f")
    nhr = st.number_input("NHR", format="%.5f")
    hnr = st.number_input("HNR", format="%.5f")
    rpde = st.number_input("RPDE", format="%.5f")
    dfa = st.number_input("DFA", format="%.5f")
    spread1 = st.number_input("spread1", format="%.5f")
    spread2 = st.number_input("spread2", format="%.5f")
    d2 = st.number_input("D2", format="%.5f")
    ppe = st.number_input("PPE", format="%.5f")

    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp,
                                                            shimmer, shimmer_db, apq3, apq5, apq, dda, nhr, hnr,
                                                            rpde, dfa, spread1, spread2, d2, ppe]])
        if parkinsons_prediction[0] == 1:
            st.error("The person has Parkinson's Disease")
        else:
            st.success("The person does not have Parkinson's Disease")
