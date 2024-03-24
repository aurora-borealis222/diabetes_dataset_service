import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='Diabetes prediction dataset preview',
    layout='wide'
)

df = st.cache_data(pd.read_csv)('data/diabetes_prediction_dataset.csv')
df.dropna(inplace=True)

st.title('Diabetes prediction dataset')

st.markdown('The Diabetes prediction dataset is a collection of medical and demographic data from patients, '
        'along with their diabetes status (positive or negative).  \nThe data includes features such as age, '
        'gender, body mass index (BMI), hypertension, heart disease, smoking history, HbA1c level,'
        ' and blood glucose level.')

st.sidebar.subheader("Parameters")

diabetes = st.sidebar.checkbox('**Diabetes**')

gender = st.sidebar.multiselect(
    'Gender',
    ['Female', 'Male'],
    'Female'
)

age = st.sidebar.slider('Age', min_value=df['age'].min(), max_value=df['age'].max(), value=20.0, step=1.0)

hypertension = st.sidebar.radio('Hypertension', ('No', 'Yes'), index=0)
hypertension_dict = {'No': 0, 'Yes': 1}

heart_disease = st.sidebar.checkbox('Heart Disease')

smoking_history = st.sidebar.selectbox('Smoking history', df['smoking_history'].unique())

bmi = st.sidebar.slider(
    'Body Mass Index (BMI)',
    min_value=df['bmi'].min(),
    max_value=df['bmi'].max(),
    value=(df['bmi'].min(), df['bmi'].max())
)

HbA1c_level = st.sidebar.slider(
    'HbA1c Level (Glycated Hemoglobin)',
    min_value=df['HbA1c_level'].min(),
    max_value=df['HbA1c_level'].max(),
    value=(df['HbA1c_level'].min(), df['HbA1c_level'].max())
)

blood_glucose_level = st.sidebar.slider(
    'Blood Glucose Level',
    min_value=df['blood_glucose_level'].min(),
    max_value=df['blood_glucose_level'].max(),
    value=(df['blood_glucose_level'].min(), df['blood_glucose_level'].max())
)

filtered = df[df['diabetes'].isin([diabetes])
              & df['gender'].isin(gender)
              & df['age'].isin([age])
              & df['hypertension'].isin([hypertension_dict[hypertension]])
              & df['heart_disease'].isin([heart_disease])
              & df['smoking_history'].isin([smoking_history])
              & df['bmi'].between(*bmi)
              & df['HbA1c_level'].between(*HbA1c_level)
              & df['blood_glucose_level'].between(*blood_glucose_level)]
st.write(filtered)
