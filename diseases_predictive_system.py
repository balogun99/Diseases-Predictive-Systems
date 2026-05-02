# load the libraries
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# load the models
diabetes_model = pickle.load(open('/Users/macbookpro/Desktop/ML & DL & GENAI Projects/Diseases Predictive System/saved models/diabetes_model.sav', 'rb'))
heart_model = pickle.load(open('/Users/macbookpro/Desktop/ML & DL & GENAI Projects/Diseases Predictive System/saved models/heart_model.sav', 'rb'))
kidney_model = pickle.load(open('/Users/macbookpro/Desktop/ML & DL & GENAI Projects/Diseases Predictive System/saved models/kidney_model.sav', 'rb'))
calories_model = pickle.load(open('/Users/macbookpro/Desktop/ML & DL & GENAI Projects/Diseases Predictive System/saved models/calorie_model.sav', 'rb'))

# sidebar
with st.sidebar:
    selected = option_menu("Diseases Predictive System", 
                           ['Diabetes Disease Prediction',
                            'Heart Disease Prediction',
                            'Kidney Disease Prediction',
                            'Calorie Burn Prediction'],
                            icons = ['activity', 'heart', 'activity', 'person'],
                            default_index=0)
    
# Diabetes Prediction
if(selected == 'Diabetes Disease Prediction'):
    # title
    st.title('Diabetes Disease Predictive System Using Machine Learning')
    # inputs from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")

    with col2:
        Glucose = st.text_input("Glucose Level")

    with col3:
        BloodPressure = st.text_input("Blood Pressure Level")

    with col1:
        SkinThickness = st.text_input("Skin Thickness Value")
    
    with col2:
        Insulin = st.text_input("Insulin Level")

    with col3:
        BMI = st.text_input("BMI Level")

    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Level")

    with col2:
        Age = st.text_input("Age of the Person")

    # prediction
    diabetes_diagnosis = ''

    # button for prediction
    if st.button('Diabetes Disease Test Result'):

        diabetes_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness,
                                                       Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if(diabetes_prediction[0] == 0):
            diabetes_diagnosis = 'Non-Diabetic Patient'
        else:
            diabetes_diagnosis = 'Diabetic Patient'

    st.success(diabetes_diagnosis)

# heart
if(selected == 'Heart Disease Prediction'):
    # title
    st.title('Heart Diseases Predictive System Using Machine Learning')

    col1, col2, col3 = st.columns(3)

    with col1:
        age  = st.text_input("Age of the Person")

    with col2:
        sex = st.text_input("Gender of the Person (0 - Female, 1 - Male)")

    with col3:
        cp = st.text_input("Chest Pain Level")

    with col1:
        trestbps = st.text_input("Resting Blood Pressure")

    with col2:
        chol = st.text_input("Serum Cholesterol Level")

    with col3:
        fbs = st.text_input("Fasting Blood Sugar Level")

    with col1:
        restecg = st.text_input("Resting Cardiographic Result")
        
    with col2:
        thalach = st.text_input("Maximum Heart Rate Achieved")
        
    with col3:
        exang = st.text_input("Exercise Induced Vagina")
        
    with col1:
        oldpeak = st.text_input("Depression Induced by Exercise")
        
    with col2:
        slope = st.text_input("Slope of the Peak Exercise")
        
    with col3:
        ca = st.text_input("Colored Flouroscopy")
        
    with col1:
        thal = st.text_input("Normal")

    # prediction
    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        
        heart_prediction = heart_model.predict([[age,sex,cp,trestbps,chol,
        	fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
        if(heart_prediction[0] == 0):
            heart_diagnosis = 'Healthy Heart'
        else:
            heart_diagnosis = 'Defective Heart'

    st.success(heart_diagnosis)

# kidney
if (selected == 'Kidney Disease Prediction'):
    
    # title
    st.title('Kidney Disease Predictive System Using Machine Learning')

    # columns
    col1, col2, col3 = st.columns(3)

    with col1:
        Age = st.text_input("Age of the Individual")
        
    with col2:
        Creatinine_Level = st.text_input("Creatinine_Level")

    with col3:
        BUN = st.text_input("BUN Level")

    with col1:
        Diabetes = st.text_input("Diabetes Status (0 - Non-Diabetic, 1 - Diabetic)")

    with col2:
        Hypertension = st.text_input("Hypertension Status (0 - No Hypertension, 1 - Yes Hypertension)")

    with col3:
        GFR = st.text_input("GFR Level")

    with col1:
        Urine_Output = st.text_input("Urine Output Level")

    with col2:
        CKD_Status = st.text_input("CKD Status")

    # prediction
    kidney_diag = ''

    if st.button('Kidney Disease Test Result'):
        kidney_prediction = kidney_model.predict([[Age,Creatinine_Level,BUN,Diabetes,
                                                   Hypertension,GFR,Urine_Output,CKD_Status]])
        
        if(kidney_prediction[0] == 1):
            kidney_diag = 'No Dialysis Present'
        else:
            kidney_diag = 'Dialysis Present'
    st.success(kidney_diag)

# calorie
if(selected == 'Calorie Burn Prediction'):
    
    # title
    st.title('Calorie Burn Predictive System Using Machine Learning')
    
    # columns
    col1, col2, col3 = st.columns(3)

    with col1:
        Gender = st.text_input("Gender (1 - Female, 0 - Male)")

    with col2:
        Age = st.text_input("Age")

    with col3:
        Height = st.text_input("Height")

    with col1:
        Weight = st.text_input("Weight")

    with col2:
        Duration = st.text_input("Duration")

    with col3:
        Heart_Rate = st.text_input("Heart Rate")

    with col1:
        Body_Temp = st.text_input("Body Temperature")

    # prediction
    calorie_prediction = ''

    if st.button('Calorie Burn Prediction Test Result'):
        
        # Gender	Age	Height	Weight	Duration	Heart_Rate	Body_Temp
        calorie_result = calories_model.predict([[Gender,Age,Height,Weight,Duration,Heart_Rate,Body_Temp]])

        if(calorie_result[0] == 0):
            calorie_prediction = 'High Calories'
        else:
            calorie_prediction = 'Low Calories'

        st.success(calorie_prediction)