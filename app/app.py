import os
import pickle
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import plotly.graph_objects as go

# Page config
st.set_page_config(page_title="Multiple Disease Prediction", layout="centered", page_icon="🩺")

# Title
st.title("🩺 Multiple Disease Prediction System")

# About the app
with st.expander("ℹ️ About this App"):
    st.markdown("""
This application helps predict the likelihood of:

- **Diabetes**
- **Heart Disease**
- **Parkinson's Disease**

Select the disease, enter the inputs, and hit Predict.  
Models are trained using supervised machine learning.

**Mohammed Asbar** is a machine learning enthusiast and this app is part of his professional portfolio.
""")

# Load model helper
def load_model(model_name):
    model_path = os.path.join("..", "multiple disease prediction", model_name)
    try:
        return pickle.load(open(model_path, "rb"))
    except FileNotFoundError:
        st.error(f"⚠️ File not found: {model_path}")
    except Exception as e:
        st.error(f"❌ Failed to load model: {e}")
    return None

# Load models
diabetes_model = load_model("diabetes_model.sav")
heart_model = load_model("heart_disease_model.sav")
parkinsons_model = load_model("parkinsons_model.sav")

# Sidebar
with st.sidebar:
    selected = option_menu("Prediction Menu",
        ["Diabetes 🩸", "Heart ❤️", "Parkinson's 🧠"],
        icons=["droplet-half", "heart-pulse", "activity"],
        default_index=0)

# =========================================
# Diabetes Section
# =========================================
if selected == "Diabetes 🩸":
    st.header("🩸 Diabetes Prediction")

    with st.form("diabetes_form"):
        col1, col2, col3 = st.columns(3)
        Pregnancies = col1.number_input("Pregnancies", min_value=0)
        Glucose = col2.number_input("Glucose Level", min_value=0)
        BloodPressure = col3.number_input("Blood Pressure", min_value=0)
        SkinThickness = col1.number_input("Skin Thickness", min_value=0)
        Insulin = col2.number_input("Insulin Level", min_value=0)
        BMI = col3.number_input("BMI", min_value=0.0)
        DPF = col1.number_input("Diabetes Pedigree Function", min_value=0.0)
        Age = col2.number_input("Age", min_value=0)

        submit = st.form_submit_button("🔎 Predict")

    if submit and diabetes_model:
        inputs = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DPF, Age]
        prediction = diabetes_model.predict([inputs])[0]
        result = "⚠️ The person is diabetic" if prediction == 1 else "✅ The person is not diabetic"
        st.success(result)

        st.subheader("📝 Input Summary")
        features = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DPF", "Age"]
        st.table(pd.DataFrame({"Feature": features, "Value": inputs}))

        st.subheader("📊 Visualization")
        st.plotly_chart(go.Figure([go.Bar(x=features, y=inputs)]), use_container_width=True)

# =========================================
# Heart Disease Section
# =========================================
elif selected == "Heart ❤️":
    st.header("❤️ Heart Disease Prediction")

    with st.form("heart_form"):
        col1, col2, col3 = st.columns(3)
        Age = col1.number_input("Age", 0)
        Sex = col2.selectbox("Sex", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
        CP = col3.selectbox("Chest Pain Type", [0,1,2,3])
        Trestbps = col1.number_input("Resting Blood Pressure", 0)
        Chol = col2.number_input("Cholesterol (mg/dl)", 0)
        FBS = col3.selectbox("Fasting Blood Sugar > 120 mg/dl", [0,1])
        RestECG = col1.selectbox("Rest ECG (0–2)", [0,1,2])
        Thalach = col2.number_input("Max Heart Rate", 0)
        ExAng = col3.selectbox("Exercise Induced Angina", [0,1])
        Oldpeak = col1.number_input("ST Depression", 0.0)
        Slope = col2.selectbox("ST Slope (0–2)", [0,1,2])
        CA = col3.selectbox("No. of Major Vessels (0–3)", [0,1,2,3])
        Thal = col1.selectbox("Thal (0=Normal, 1=Fixed, 2=Reversible)", [0,1,2])

        submit = st.form_submit_button("🔎 Predict")

    if submit and heart_model:
        inputs = [Age, Sex, CP, Trestbps, Chol, FBS, RestECG, Thalach,
                  ExAng, Oldpeak, Slope, CA, Thal]
        prediction = heart_model.predict([inputs])[0]
        result = "⚠️ The person has heart disease" if prediction == 1 else "✅ No heart disease detected"
        st.success(result)

        st.subheader("📝 Input Summary")
        features = ["Age","Sex","CP","BP","Chol","FBS","RestECG","Thalach",
                    "ExAng","OldPeak","Slope","CA","Thal"]
        st.table(pd.DataFrame({"Feature": features, "Value": inputs}))

        st.subheader("📊 Visualization")
        st.plotly_chart(go.Figure([go.Bar(x=features, y=inputs)]), use_container_width=True)

# =========================================
# Parkinson's Section
# =========================================
elif selected == "Parkinson's 🧠":
    st.header("🧠 Parkinson's Prediction")

    with st.form("parkinsons_form"):
        features = [
            "Fo", "Fhi", "Flo", "Jitter%", "JitterAbs", "RAP", "PPQ", "DDP",
            "Shimmer", "Shimmer_dB", "APQ3", "APQ5", "APQ", "DDA", "NHR", "HNR",
            "RPDE", "DFA", "spread1", "spread2", "D2", "PPE"
        ]
        values = [st.number_input(feature, value=0.0) for feature in features]
        submit = st.form_submit_button("🔎 Predict")

    if submit and parkinsons_model:
        prediction = parkinsons_model.predict([values])[0]
        result = "⚠️ The person has Parkinson's disease" if prediction == 1 else "✅ No Parkinson's detected"
        st.success(result)

        st.subheader("📝 Input Summary")
        st.table(pd.DataFrame({"Feature": features, "Value": values}))

        st.subheader("📊 Visualization")
        st.plotly_chart(go.Figure([go.Bar(x=features[:10], y=values[:10])]), use_container_width=True)