import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.graph_objects as go
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Multiple Disease Prediction System",
    page_icon="🩺",
    layout="centered"
)

# Load the models
diabetes_model = pickle.load(open(r"C:\Users\Asbar\OneDrive\Desktop\desease predictor\multiple disease prediction\diabetes_model.sav",'rb'))
heart_disease_model = pickle.load(open(r"C:\Users\Asbar\OneDrive\Desktop\desease predictor\multiple disease prediction\heart_disease_model.sav",'rb'))
parkinsons_model = pickle.load(open(r"C:\Users\Asbar\OneDrive\Desktop\desease predictor\multiple disease prediction\parkinsons_model.sav",'rb'))

# Title of the app
st.title("🩺 Multiple Disease Prediction System")

# About the App Section
with st.expander("ℹ️ About this App"):
    st.write("""
    This application allows you to predict the likelihood of:
    - **Diabetes**
    - **Heart Disease**
    - **Parkinson's Disease**

    Simply select the disease type, enter the required medical information, and click predict.
    The models used are trained using supervised machine learning algorithms.
    
    Mohammed Asbar is a machine learning enthusiast and this app is part of his portfolio
    """)

# Sidebar navigation
with st.sidebar:
    selected = option_menu(
        'Prediction Menu',
        ['Diabetes Prediction 🩸', 'Heart Disease Prediction ❤️', 'Parkinsons Prediction 🧠'],
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# ================================
# Diabetes Prediction Page
# ================================
if selected == 'Diabetes Prediction 🩸':
    st.header('🩸 Diabetes Prediction')

    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')

    diab_diagnosis = ''
    if st.button('🔎 Get Diabetes Test Result'):
        feature_names = ['Pregnancies','Glucose','BloodPressure','SkinThickness',
                        'Insulin','BMI','DiabetesPedigreeFunction','Age']
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        user_input_float = [float(x) for x in user_input]

        # Show input table
        st.subheader("📝 Input Features Summary")
        df = pd.DataFrame({'Feature': feature_names, 'Value': user_input_float})
        st.table(df)

        # Visualization
        st.subheader("📊 Input Visualization")
        fig = go.Figure([go.Bar(x=feature_names, y=user_input_float)])
        st.plotly_chart(fig, use_container_width=True)

        diab_prediction = diabetes_model.predict([user_input_float])
        if diab_prediction[0] == 1:
            diab_diagnosis = '⚠️ The person is diabetic'
        else:
            diab_diagnosis = '✅ The person is not diabetic'
    st.success(diab_diagnosis)

# ================================
# Heart Disease Prediction Page
# ================================
if selected == 'Heart Disease Prediction ❤️':
    st.header('❤️ Heart Disease Prediction')

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain types')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    heart_diagnosis = ''
    if st.button('🔎 Get Heart Disease Test Result'):
        feature_names = ['Age','Sex','CP','BP','Chol','FBS','RestECG','Thalach',
                        'ExAng','OldPeak','Slope','CA','Thal']
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach,
                    exang, oldpeak, slope, ca, thal]
        user_input_float = [float(x) for x in user_input]

        # Show input table
        st.subheader("📝 Input Features Summary")
        df = pd.DataFrame({'Feature': feature_names, 'Value': user_input_float})
        st.table(df)

        # Visualization
        st.subheader("📊 Input Visualization")
        fig = go.Figure([go.Bar(x=feature_names, y=user_input_float)])
        st.plotly_chart(fig, use_container_width=True)

        heart_prediction = heart_disease_model.predict([user_input_float])
        if heart_prediction[0] == 1:
            heart_diagnosis = '⚠️ The person is having heart disease'
        else:
            heart_diagnosis = '✅ The person does not have any heart disease'
    st.success(heart_diagnosis)

# ================================
# Parkinson's Prediction Page
# ================================
if selected == 'Parkinsons Prediction 🧠':
    st.header("🧠 Parkinson's Prediction")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col1:
        RAP = st.text_input('MDVP:RAP')
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
    with col3:
        DDP = st.text_input('Jitter:DDP')
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
    with col3:
        APQ = st.text_input('MDVP:APQ')
    with col4:
        DDA = st.text_input('Shimmer:DDA')
    with col5:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('spread1')
    with col5:
        spread2 = st.text_input('spread2')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')

    parkinsons_diagnosis = ''
    if st.button("🔎 Get Parkinson's Test Result"):
        feature_names = ['Fo','Fhi','Flo','Jitter%','JitterAbs','RAP','PPQ','DDP',
                        'Shimmer','Shimmer_dB','APQ3','APQ5','APQ','DDA','NHR','HNR',
                        'RPDE','DFA','spread1','spread2','D2','PPE']
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP,
                    Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR,
                    RPDE, DFA, spread1, spread2, D2, PPE]
        user_input_float = [float(x) for x in user_input]

        # Show input table
        st.subheader("📝 Input Features Summary")
        df = pd.DataFrame({'Feature': feature_names, 'Value': user_input_float})
        st.table(df)

        # Visualization (only 10 features for better view)
        st.subheader("📊 Input Visualization")
        fig = go.Figure([go.Bar(x=feature_names[:10], y=user_input_float[:10])])
        st.plotly_chart(fig, use_container_width=True)

        parkinsons_prediction = parkinsons_model.predict([user_input_float])
        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "⚠️ The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "✅ The person does not have Parkinson's disease"
    st.success(parkinsons_diagnosis)
