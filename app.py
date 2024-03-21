
import streamlit as st
import utils
from keras.models import load_model
#import pickle 
import keras
import time
import pandas as pd

model = load_model('Models/model.h5')

def step_1():
    st.title("FORMULAIRE")
    engine=  st.text_input("Engine")
    cylinder = st.text_input("Cyliender")
    Fuelconsumption_comb = st.text_input("Fuelconsumption_comb")
   
    
    return engine, cylinder, Fuelconsumption_comb



def step_3():
    st.title("File: Upload CSV")
    csv_file = st.file_uploader("Choisir un CSV",  type = ['csv'])
    return csv_file

    
def reset():
   engine, cylinder, Fuelconsumption_comb = "", "", "", ""
  
   csv_file = None

def main():
    st.sidebar.title("ASSISTANT FORMULAIRE") 
    current_step = st.sidebar.selectbox("input type", ["Credentiel", "File"])
    
    
    if current_step == "Credentiel":
        engine, cylinder, Fuelconsumption_comb = step_1() 
        if engine and cylinder and Fuelconsumption_comb:
            pred = utils.prediction(engine, cylinder, Fuelconsumption_comb, model)  
            st.success(pred)     
    
    
    
    elif current_step == "File":
        csv_file = step_3()
        next_step_button = st.sidebar.button("Submit")
        if next_step_button:
            utils.csv_prediction(csv_file, model)
            data = pd.read_csv('csv/prediction.csv')
            st.dataframe(data)
    
    
    if st.sidebar.button("Reset", key="reset"):
        engine, cylinder, Fuelconsumption_comb = "", "", ""
        csv_file = None

if __name__ == "__main__":
    main()