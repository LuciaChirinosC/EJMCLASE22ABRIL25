import streamlit as st
import pandas as pd
from utils.data_processing import clean_data
from utils.visualization import plot_price_distribution

#Cargar los datos
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/anfagudelogo-tpt/datasets/refs/heads/main/car_price_dataset.csv')
df=clean_data(df)

#Titulo y descripcion de la app
st.title("Analisis Descriptivo de Vehiculos")
st.write("Esta aplicacion permite explorar un dataset de vehiculos, proporcionando estditias y visualizacion interactivas")

#Mostrar el resumen estadistico
tabla_resumen=df.describe()
st.write("### Resumen Estadistico de los Datos")
st.dataframe(tabla_resumen)

#Generar y mostrar graficos
fig1=plot_price_distribution(df)
st.pyplot(fig1)