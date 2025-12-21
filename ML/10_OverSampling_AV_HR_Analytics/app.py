#pip install streamlit

import streamlit as st
import pandas as pd
import joblib

st.title("HR job Look Prediction")

#from pathlib import Path
### This gets the absolute path of the directory where app.py lives
###current_dir = Path(__file__).parent
###file_path = current_dir / "train.csv"
###df = pd.read_csv(file_path)

df = pd.read_csv('train.csv')

#input fields

city = st.selectbox('city', pd.unique(df['city']))                    
city_development_index  = st.number_input('city_development_index')
gender = st.selectbox('gender', pd.unique(df['gender']))                    
relevent_experience = st.selectbox('relevent_experience', pd.unique(df['relevent_experience']))        
enrolled_university =  st.selectbox('enrolled_university', pd.unique(df['enrolled_university']))   
education_level  =   st.selectbox('education_level', pd.unique(df['education_level']))          
major_discipline  = st.selectbox('major_discipline', pd.unique(df['major_discipline']))     
experience = st.selectbox('experience', pd.unique(df['experience']))             
company_size = st.selectbox('company_size', pd.unique(df['company_size']))              
company_type   = st.selectbox('company_type', pd.unique(df['company_type']))           
last_new_job   = st.selectbox('last_new_job', pd.unique(df['last_new_job']))         
training_hours  =   st.number_input('training_hours')      

#o/p
#target
inputs = {
    'city' : city,
    'city_development_index' : city_development_index,
    'gender' : gender,
    'relevent_experience' : relevent_experience,
    'enrolled_university' : enrolled_university,
    'education_level' : education_level,
    'major_discipline' : major_discipline,
    'experience' : experience,
    'company_size' : company_size,
    'company_type' : company_type,
    'last_new_job' : last_new_job,
    'training_hours' : training_hours,
}

if st.button('Predict'):
    model = joblib.load('jobchg_pipeline_model.pkl')
    X_input = pd.DataFrame([inputs])
    prediction = model.predict(X_input)
    st.write(prediction)
    st.balloons()