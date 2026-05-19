
import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # lendo os dados

# cabeçalho
st.header('Análise de anúncios de vendas de carros')

# caixa de seleção para histograma
build_histogram = st.checkbox('Criar um histograma')

if build_histogram:
    st.write('Criando um histograma para a coluna odometer')

    # criar histograma
    fig = px.histogram(car_data, x='odometer')

    # mostrar gráfico
    st.plotly_chart(fig, use_container_width=True)

# caixa de seleção para gráfico de dispersão
build_scatter = st.checkbox('Criar um gráfico de dispersão')

if build_scatter:
    st.write('Criando um gráfico de dispersão entre odometer e price')

    # criar gráfico de dispersão
    fig = px.scatter(car_data, x='odometer', y='price')

    # mostrar gráfico
    st.plotly_chart(fig, use_container_width=True)
