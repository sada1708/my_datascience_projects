import streamlit as st
import pandas as pd
import numpy as np
import joblib
from model_dataPrep import data_prep

@st.cache_resource
def load_assets():
    model = joblib.load('house_price_model.pkl')
    defaults = joblib.load('model_defaults.joblib')
    return model, defaults

model, defaults = load_assets()
df = pd.read_csv('train.csv')

st.title('House Price Prediction')
st.write('Enter the details of the house to estimate its market value.')

col1, col2 = st.columns(2)

with col1:
    user_LotArea = st.number_input("Total Lot Area (sgft)", value = 3000)
    user_Neighborhood = st.selectbox('Neighborhood',pd.unique(df['Neighborhood']))
    user_BldgType = st.selectbox('Building Type', pd.unique(df['BldgType']))
    user_HouseStyle = st.selectbox('House Style', pd.unique(df['HouseStyle']))
    user_YearBuilt = st.slider('Year Built', 1996,2010, 2004)
    user_YearRemodAdd = st.slider('Year Remodelled', 1996,2010, 2004)


with col2:
    user_GrLivArea = st.slider('Total Living area (sqft)', 1800, 4000, 2200)
    user_Utilities = st.selectbox('Utilities', pd.unique(df['Utilities']))
    user_OverallQuality = st.slider("Overall Quality (1-10)", 1, 10, 5)
    user_OverallCond = st.slider("Overall Condition (1-10)", 1, 10, 5)
    user_FullBath = st.selectbox('Num of Full Bath', [1,2,3,4])
    user_Bedroom = st.selectbox('Num of Bedrooms', [1,2,3,4])

if st.button('Predict'):
    # Input default values, full dict with all default values
    input_data = defaults.copy()

    #Overwrite user inputs on the dict to replace default values
    input_data['LotArea'] = user_LotArea
    input_data['Neighborhood'] = user_Neighborhood
    input_data['BldgType'] = user_BldgType
    input_data['HouseStyle'] = user_HouseStyle
    input_data['YearBuilt'] = user_YearBuilt
    input_data['YearRemodAdd'] = user_YearRemodAdd   
    input_data['GrLivArea'] = user_GrLivArea
    input_data['Utilities'] = user_Utilities
    input_data['OverallQual'] = user_OverallQuality   
    input_data['OverallCond'] = user_OverallCond
    input_data['FullBath'] = user_FullBath
    input_data['Bedroom'] = user_Bedroom

    input_df = pd.DataFrame([input_data])
    input_df = data_prep(input_df)

    price = np.expm1x(model.predict(input_df)[0])

    st.metric('Estimated Value', f'${price:,.2f}')
    st.balloons()

  
