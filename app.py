import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
st.header('Análisis de carros')  # crear encabezado
build_histogram = st.checkbox('Construir histograma')  # crear una casilla de verificación

if build_histogram:  # si la casilla de verificación está seleccionada
    # escribir un mensaje
    st.write('Construir un histograma para la columna odómetro')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Construir gráfico de dispersión')  # crear una casilla de verificación

if build_scatter:  # si la casilla de verificación está seleccionada
    # escribir un mensaje
    st.write('Construir un gráfico de dispersión para la columna odómetro')

    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y='price')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
