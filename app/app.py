import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.graph_objects as go

# Set page config
st.set_page_config(page_title="Multiple Disease Predictor", layout="centered", page_icon="🩺")


# Load models safely
def load_model(filename):
    try:
        return pickle.load(open(os.path.join("..", "multiple disease prediction", filename), "rb"))
    except Exception as e:
        st.error(f"Model loading failed: {e}")
        return None

diabetes_model = load_model("diabetes_model.sav")
heart_model = load_model("heart_disease_model.sav")
parkinsons_model = load_model("parkinsons_model.sav")

st.title("🩺 Multiple Disease Prediction System")
# About the App
with st.expander("ℹ️ About this App"):
    st.markdown("""
This application helps predict the likelihood of:

- **Diabetes**
- **Heart Disease**
- **Parkinson's Disease**

Simply select the disease type, input medical data, and click predict.  
Each model is trained using supervised machine learning.

**Mohammed Asbar** is a machine learning enthusiast, and this app is part of his professional portfolio.
""")

with st.sidebar:
    choice = option_menu("Prediction Menu", 
                        ["Diabetes 🩸", "Heart ❤️", "Parkinson's 🧠"],
                        icons=["droplet-half", "heart-pulse", "activity"],
                        default_index=0)

# ========== DIABETES ==========
if choice == "Diabetes 🩸":
    st.header("🩸 Diabetes Prediction")
    with st.form("diabetes_form"):
        cols = st.columns(4)
        inputs = {
            "Pregnancies": cols[0].number_input("Pregnancies", 0.0),
            "Glucose": cols[1].number_input("Glucose Level", 0.0),
            "BloodPressure": cols[2].number_input("Blood Pressure", 0.0),
            "SkinThickness": cols[3].number_input("Skin Thickness", 0.0),
            "Insulin": cols[0].number_input("Insulin Level", 0.0),
            "BMI": cols[1].number_input("BMI", 0.0),
            "DiabetesPedigreeFunction": cols[2].number_input("Diabetes Pedigree Function", 0.0),
            "Age": cols[3].number_input("Age", 0.0)
        }
        submitted = st.form_submit_button("🔎 Predict")

    if submitted and diabetes_model:
        input_list = list(inputs.values())
        prediction = diabetes_model.predict([input_list])
        diagnosis = "⚠️ Diabetic" if prediction[0] else "✅ Not Diabetic"
        st.success(diagnosis)
        st.subheader("📊 Input Summary")
        st.table(pd.DataFrame({"Feature": inputs.keys(), "Value": input_list}))
        st.plotly_chart(go.Figure([go.Bar(x=list(inputs.keys()), y=input_list)]), use_container_width=True)

# ========== HEART ==========
elif choice == "Heart ❤️":
    st.header("❤️ Heart Disease Prediction")
    with st.form("heart_form"):
        cols = st.columns(4)
        inputs = {
            "Age": cols[0].number_input("Age", 0),
            "Sex": cols[1].number_input("Sex (1=Male, 0=Female)", 0),
            "CP": cols[2].number_input("Chest Pain Type (0–3)", 0),
            "BP": cols[3].number_input("Resting BP", 0),
            "Chol": cols[0].number_input("Cholesterol", 0),
            "FBS": cols[1].number_input("Fasting Blood Sugar >120 (1=True)", 0),
            "RestECG": cols[2].number_input("Rest ECG (0–2)", 0),
            "Thalach": cols[3].number_input("Max Heart Rate", 0),
            "ExAng": cols[0].number_input("Exercise Induced Angina (1=True)", 0),
            "OldPeak": cols[1].number_input("ST Depression", 0.0),
            "Slope": cols[2].number_input("ST Slope (0–2)", 0),
            "CA": cols[3].number_input("Major Vessels Colored", 0),
            "Thal": cols[0].number_input("Thal (0=Normal, 1=Fixed, 2=Reversible)", 0)
        }
        submitted = st.form_submit_button("🔎 Predict")

    if submitted and heart_model:
        input_list = list(inputs.values())
        prediction = heart_model.predict([input_list])
        diagnosis = "⚠️ At risk of heart disease" if prediction[0] else "✅ No heart disease detected"
        st.success(diagnosis)
        st.subheader("📊 Input Summary")
        st.table(pd.DataFrame({"Feature": inputs.keys(), "Value": input_list}))
        st.plotly_chart(go.Figure([go.Bar(x=list(inputs.keys()), y=input_list)]), use_container_width=True)

# ========== PARKINSON'S ==========
else:
    st.header("🧠 Parkinson's Disease Prediction")
    with st.form("parkinsons_form"):
        features = [
            "Fo", "Fhi", "Flo", "Jitter%", "JitterAbs", "RAP", "PPQ", "DDP",
            "Shimmer", "Shimmer_dB", "APQ3", "APQ5", "APQ", "DDA", "NHR", "HNR",
            "RPDE", "DFA", "spread1", "spread2", "D2", "PPE"
        ]
        values = [st.number_input(f"{f}", 0.0) for f in features]
        submitted = st.form_submit_button("🔎 Predict")

    if submitted and parkinsons_model:
        prediction = parkinsons_model.predict([values])
        diagnosis = "⚠️ Has Parkinson's disease" if prediction[0] else "✅ No Parkinson's detected"
        st.success(diagnosis)
        st.subheader("📊 Input Summary")
        st.table(pd.DataFrame({"Feature": features, "Value": values}))
        st.plotly_chart(go.Figure([go.Bar(x=features[:10], y=values[:10])]), use_container_width=True)