import streamlit as st
import requests

st.title("Classificador de Pinguins 🐧")

st.sidebar.header("Informe os dados do pinguim:")

bill_length = st.sidebar.slider("Comprimento do bico (mm)", 30.0, 60.0, 45.0)
bill_depth = st.sidebar.slider("Profundidade do bico (mm)", 13.0, 21.0, 17.0)
flipper_length = st.sidebar.slider("Comprimento da nadadeira (mm)", 170, 240, 200)
body_mass = st.sidebar.slider("Massa corporal (g)", 2500, 6500, 4000)

if st.button("Prever espécie"):
    entrada = {
        "bill_length_mm": bill_length,
        "bill_depth_mm": bill_depth,
        "flipper_length_mm": flipper_length,
        "body_mass_g": body_mass
    }
    # Envia os dados para a API
    response = requests.post("http://127.0.0.1:8000/predict", json=entrada)

    if response.status_code == 200:
        especie = response.json()["species"]
        st.success(f"A espécie predita é: **{especie}**")
    else:
        st.error("Erro ao conectar com a API.")
