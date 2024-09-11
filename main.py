#imoprtar bibliotecas
import streamlit as st
import pandas as pd
import yfinance as yf


#criar funções de acrregamento de dados
    #cotações do itau -ITUB4 - 2010 a 2024

@st.cache_data
def carregar_dados(empresa):
    dados_acao = yf.Ticker(empresa)
    cotacoes_acao = dados_acao.history(period="1d",start="2010-01-01",end="2024-07-01")
    cotacoes_acao = cotacoes_acao[["Close"]]
    return cotacoes_acao


# prepara as visualizações
dados= carregar_dados("ITUB4.SA")

#criar a interface do streamlit
st.write(""" 
# App preço de Ações
O gráfico abaixo representa a evolução do preço das ações do Itaú (ITUB4) ao longo dos anos
""") #markdown

#criar o gráfico
st.line_chart(dados)

st.write("""
#Fim do app
""")