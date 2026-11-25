# Estudo de Caso 1 - DSA AI Coder - Criando seu Assistente de Programção Python, em Python

# Importa o módulo para interagir com o sistema operacional
import os

# Importa a biblioteca Streamlit para criar a interface web interativa
import streamlit as st

# Importa a classe Groq para se conectar à API da plataforma Groq e acessar o LLM
from groq import Groq

# Configura a página do Streamlit com título, ícone, layout e estado inicial da sidebar
st.set_page_config(
    page_title="DSA AI Coder",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)