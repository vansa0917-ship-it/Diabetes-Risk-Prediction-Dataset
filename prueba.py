import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px 
import streamlit as st

st.title("Análisis de Riesgo de Diabetes")

st.write("""Este proyecto analiza un dataset de factores de riesgo de diabetes
como edad, IMC, presión arterial y glucosa para identificar patrones
asociados al riesgo de desarrollar la enfermedad.
""")

st.header("Objetivos")

st.write("""- Analizar factores de riesgo asociados a la diabetes.
- Identificar patrones en variables como edad, glucosa y BMI.
- Visualizar tendencias y distribución de los datos.
""")
#-------

@st.cache_data
def load_data():
    return pd.read_csv("diabetes_risk_dataset.csv")
df = load_data()
st.sidebar.header("Filtros")
edad = st.sidebar.slider("Edad",int(df["age"].dropna().min()),int(df["age"].dropna().max()),(20,84))
df = df[(df["age"] >= edad[0]) & (df["age"] <= edad[1])]
#-------

@st.cache_data
def load_data():
    return pd.read_csv("diabetes_risk_dataset.csv")
df = load_data()
st.sidebar.header("Filtros")
imc = st.sidebar.slider("IMC",int(df["bmi"].dropna().min()),int(df["bmi"].dropna().max()),(20,84))
df = df[(df["bmi"] >= imc[0]) & (df["bmi"] <= imc[1])]
#-------

@st.cache_data
def load_data():
    return pd.read_csv("diabetes_risk_dataset.csv")
df = load_data()
st.sidebar.header("Filtros")
edad = st.sidebar.slider("Edad",int(df["age"].dropna().min()),int(df["age"].dropna().max()),(20,84))
df = df[(df["age"] >= edad[0]) & (df["age"] <= edad[1])]

