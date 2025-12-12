# Framework building interactive web application directly from python without an UI
import streamlit as st
import pandas as pd
import joblib

# Load the pre-trained model
model = joblib.load('bigmart_model.pkl')
print(model)  # Debugging line to check if the model is loaded correctly

with st.form(key='input_form'): 
    st.header (" Enter the details of the product and Outlet to predict sales")
    col1, col2 = st.columns(2)
    with col1:
        Item_Weight = st.number_input('Item Weight (in grams)', min_value = 0.0, step=0.1)
        Item_Visibility = st.number_input('Item Visibility (0 to 1)', min_value=0.0, max_value=1.0, step=0.01)
        Item_MRP = st.number_input('Item MRP (in $)', min_value = 0.0, step = 0.1)
        Outlet_age = st.number_input('Outlet Age (in years)', min_value = 0, step = 1)
        Outlet_Location_Score = st.selectbox('Outlet Location Score', [1,2,3])
    
    with col2:
        Item_Type = st.text_input('Item Type (e.g. Diary, Meat, Soft Drinks etc.)')
        Item_Category = st.selectbox('Item Category', ['FD', 'NC', 'DR'])
        Outlet_Size = st.selectbox('Outlet Size', ['Small', 'Medium', 'High'])
        Outlet_Location_Type = st.selectbox('Outlet Location Type', ['Tier 1', 'Tier 2', 'Tier 3'])
        Outlet_Type = st.selectbox('Outlet Type', ['Grocery Store', 'Supermarket Type1', 'Supermarket Type2', 'Supermarket Type3'])
        Outlet_Identifier = st.selectbox('Outlet Identifier', ['OUT010', 'OUT013', 'OUT017', 'OUT018', 'OUT019', 'OUT027', 'OUT035', 'OUT045', 'OUT046', 'OUT049'])

    # values = st.text_input("Enter multiple MPRs")
    # m_values = [float(v) for v in values.split(',')]
    # st.write("MRPs entered:",m_values)
    #uploaded = st.file_uploder("Enter your CSV",type = ['csv','xlsx'])
    #data = pd.read_csv(uploaded)

    submitted = st.form_submit_button('Predict Sales')

    if submitted:
        input_data = pd.DataFrame({
            'Item_Weight': [Item_Weight],
            'Item_Visibility': [Item_Visibility],
            'Item_MRP': [Item_MRP],
            'Outlet_Age': [Outlet_age],
            'Outlet_Location_Score': [Outlet_Location_Score],
            'Item_Type': [Item_Type],
            'Item_Category': [Item_Category],
            'Outlet_Size': [Outlet_Size],
            'Outlet_Location_Type': [Outlet_Location_Type],
            'Outlet_Type': [Outlet_Type],
            'Outlet_Identifier': [Outlet_Identifier]
        })

        prediction = model.predict(input_data)
        st.success(f'Predicted Sales: $ {prediction[0]:.2f}')
        st.balloons()
        