import streamlit as st
import pandas as pd
import numpy as np
import joblib
from model_dataPrep import data_prep

@st.cache_resource
def load_assets():
    return joblib.load('hr_promotion_best_pipeline.pkl')

model = load_assets()

st.title('HR Promotion Probability Predictior')
st.write('Please enter employee details to predict promotion probability')

# 3. Create Input Form
with st.form("employee_data"):
    col1, col2 = st.columns(2)
    
    with col1:
        department = st.selectbox("Department", ['Sales & Marketing', 'Operations', 'Technology', 'Analytics', 'R&D', 'Procurement', 'Finance', 'HR', 'Legal'])
        region = st.selectbox("Region", [f'region_{i}' for i in range(1, 35)])
        education = st.selectbox("Education", ["Below Secondary", "Bachelor's", "Master's & above"])
        gender = st.selectbox("Gender", ['m', 'f'])
        recruitment_channel = st.selectbox("Recruitment Channel", ['other', 'sourcing', 'referred'])

    with col2:
        no_of_trainings = st.number_input("Number of Trainings", min_value=1, max_value=10, value=1)
        age = st.slider("Age", 18, 60, 30)
        previous_year_rating = st.slider("Previous Year Rating", 0.0, 5.0, 3.0)
        length_of_service = st.number_input("Length of Service (Years)", min_value=1, max_value=40, value=5)
        kpis_met = st.radio("KPIs Met > 80%", [1, 0], index=1)
        awards_won = st.radio("Awards Won?", [1, 0], index=1)
        avg_training_score = st.number_input("Avg Training Score", min_value=0, max_value=100, value=50)

    submit = st.form_submit_button("Predict Promotion")

# 4. Prediction Logic
if submit:
    # Create a dataframe matching your training columns
    input_data = pd.DataFrame({
        'department': [department], 'region': [region], 'education': [education],
        'gender': [gender], 'recruitment_channel': [recruitment_channel],
        'no_of_trainings': [no_of_trainings], 'age': [age],
        'previous_year_rating': [previous_year_rating], 'length_of_service': [length_of_service],
        'KPIs_met >80%': [kpis_met], 'awards_won?': [awards_won],
        'avg_training_score': [avg_training_score]
    })

    input_df = data_prep(input_data)
    # Get Prediction and Probability
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    # 5. Display Result
    st.divider()
    if prediction == 1:
        st.success(f"**PROMOTION LIKELY** (Confidence: {probability:.2%})")
        st.balloons()
    else:
        st.warning(f"**PROMOTION UNLIKELY** (Confidence: {1-probability:.2%})")



