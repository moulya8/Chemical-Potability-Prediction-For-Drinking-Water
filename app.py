

import pickle
import streamlit as st
import numpy as np
import pandas as pd




#loding the saved model

random_forest_model=pickle.load(open('random_forest_models.pickel','rb'))
standar_scaler=pickle.load(open('standar_scaler.pickel','rb'))

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://live.staticflickr.com/2474/3661497773_5c91342970_c.jpg");
background-size: 160%;
background-position: fit;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;

}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.set_option('deprecation.showfileUploaderEncoding', False)

#silde bar for navigation

#page title
st.title('A Chemical Potability Prediction For Drinking Water')

ph =st.number_input("Enter PH Level",min_value=0.,max_value=14.,step=1.,format="%f")
Hardness=st.number_input("Enter the  value of Hardness",min_value=45.,max_value=400.,step=1.,format="%f")
Solids=st.number_input('Enter the value of Solids',min_value=300.,max_value=70000.,step=1.,format="%f")
Chloramines=st.number_input("Enter the value of Chloramines",min_value=0.,max_value=14.,step=1.,format="%f")
Sulfate=st.number_input("Enter the value of Sulfate",min_value=120.,max_value=500.,step=1.,format="%f")
Conductivity=st.number_input("Enter the value of Conductivity",min_value=160.,max_value=800.,step=1.,format="%f")
Trihalomethanes=st.number_input("Enter the value of Trihalomethanes",min_value=0.,max_value=130.,step=1.,format="%f")
Turbidity=st.number_input("Enter the value of Turbidity",min_value=1.,max_value=7.,step=1.,format="%f")
Organic_carbon=st.number_input("Enter the value of Organic_carbon",min_value=1.,max_value=30.,step=1.,format="%f")

data=[[ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity]]
#sacler_data=standar_scaler.fit_transform(data)
    
predicted=''   
if st.button('Press Here to predict'):
    prd=random_forest_model.predict(data) 
    if prd==0:
       predicted="Your Water Is Not Protable"    
    else:
       predicted="Your Water Is Protable"
st.success(predicted)       
        
    
    
    
    
    
    
    
    
    
    
 
    
    
    
    
