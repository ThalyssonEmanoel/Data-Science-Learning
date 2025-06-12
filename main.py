import pandas as pd
import plotly.express as px
import streamlit as st

st.title("📊 Titanic Dashboard")

if 'df_titanic' not in st.session_state:
    st.session_state['df_titanic'] = pd.read_csv("./dataset/titanic3.csv", low_memory=False, on_bad_lines='skip')

df = st.session_state['df_titanic']#data

st.sidebar.header("Filtros")

sex_options = df['sex'].dropna().unique().tolist()
sex_selected = st.sidebar.multiselect("Sexo", options=sex_options, default=sex_options)

class_options = sorted(df['pclass'].dropna().unique().tolist())
class_selected = st.sidebar.multiselect("Classe", options=class_options, default=class_options)

# Filtro do sexo e da classe ;]
df_filtered = df[(df['sex'].isin(sex_selected)) & (df['pclass'].isin(class_selected))]

st.header("Informações Gerais")

total_passengers = len(df_filtered)
st.subheader(f"Total de passageiros: {total_passengers}")

if 'age' in df_filtered.columns:
    # Tem que converter a idade pra número, porque as vezes vem como texto ou Ccom vírgula(formato do excel ai)
    df_filtered['age'] = df_filtered['age'].astype(str).str.replace(',', '.')
    df_filtered['age'] = pd.to_numeric(df_filtered['age'], errors='coerce')
    mean_age = df_filtered['age'].mean()
    st.subheader(f"Média de idade: {mean_age:.2f}")
else:
    st.subheader("Média de idade: Não disponível")

if 'sex' in df_filtered.columns:
    sex_counts = df_filtered['sex'].value_counts()
    st.subheader(f"Quantidade de homens: {sex_counts.get('male', 0)}")
    st.subheader(f"Quantidade de mulheres: {sex_counts.get('female', 0)}")
else:
    st.subheader("Quantidade de homens e mulheres: Não disponível")

if 'pclass' in df_filtered.columns:
    class_counts = df_filtered['pclass'].value_counts().sort_index()
    for c in class_options:
        st.subheader(f"Quantidade de passageiros na classe {c}: {class_counts.get(c, 0)}")
else:
    st.subheader("Quantidade de passageiros por classe: Não disponível")

st.header("Gráficos")

if 'sex' in df_filtered.columns:
    fig_pie = px.pie(df_filtered, names='sex', title='Proporção de Homens e Mulheres')
    st.plotly_chart(fig_pie)
else:
    st.info("Coluna 'sex' não encontrada para o gráfico de pizza.")

if 'pclass' in df_filtered.columns:
    # Aqui prepara os dados pra fazer o gráfico de barras, tem que resetar o index e renomear as colunas, problema do próprio Plotly
    class_counts = df_filtered['pclass'].value_counts().sort_index().reset_index()
    class_counts.columns = ['Classe', 'Quantidade']
    fig_bar = px.bar(
        class_counts,
        x='Classe',
        y='Quantidade',
        labels={'Classe': 'Classe', 'Quantidade': 'Quantidade'},
        title='Total de Passageiros por Classe'
    )
    st.plotly_chart(fig_bar)
else:
    st.info("Coluna 'pclass' não encontrada para o gráfico de barras.")