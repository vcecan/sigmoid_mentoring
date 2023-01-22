import streamlit as st
import pandas as pd
import csv
import os
data = open(r'D:\univer\Sigmoid mentoring\Sigmoid_tasks\Streamlit\heart.csv')
data = pd.read_csv(data)
st.write(data)
age = st.number_input("Input age",0,100)
gender = st.select_slider('Choose gender',["Male","Female"])
chest_pain = st.selectbox("Choose chest pain",['TA', 'ATA','NAP','ASY'])
restingbp = st.number_input('Input resting blood pressure',90,300)
cholesterol = st.number_input("Input cholesterol value",0,500)
fastingbp = st.select_slider('Fasting blood sugar',["FastingBS < 120 mg","FastingBS > 120 mg"])
if fastingbp == "FastingBS < 120 mg":
    fastingbp = 0
else :
    fastingbp = 1
restingecg = st.selectbox("resting electrocardiogram results",['Normal','ST', 'LVH'])
maxhr = st.number_input("maximum heart rate:",6,202)
exerciseAngina = st.selectbox('Exercise-induced angina',['Y','N'])
oldpeak = st.number_input("input value measured in depression",0.0,100.0)
st_slope = st.selectbox('the slope of the peak exercise ST segment',['Up','Flat','Down'])

columns = ['Age','Sex','ChestPainType','RestingBp','Cholesterol','FastingBS','RestingEcG','MaxHR','ExerciseAngina','Oldpeak','ST_Slope']

def predict_heart():
    
  
# check if file exists
    if os.path.exists("file.csv"):
          os.remove("file.csv")
    row = [age,gender,chest_pain,restingbp,cholesterol,fastingbp,restingecg,maxhr,exerciseAngina,oldpeak,st_slope]
    f = open('file.csv', 'w',encoding='UTF8',newline = '')
    writer = csv.writer(f)
    # write the header
    writer.writerow(columns)
    # write the data
    writer.writerow(row)
    f.close()
#X=pd.DataFrame([row], columns=columns)
st.button('Predict',on_click = predict_heart)
