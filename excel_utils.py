import streamlit as st
import pandas as pd
from logic import analyse


def readExcel(api_key):
    # upload documents
    st.header("Chat para analisar documentos")

    with st.sidebar:
        st.title("Documentos")
        files = st.file_uploader(
            label="Anexar arquivos Excel",
            type=["xlsx", "xls", "csv"],
            accept_multiple_files=True,
        )

    # get user question
    user_question = st.text_input("Digite sua pergunta")

    if files is None:
        st.write("arquivo não encontrado")

    if files is not None:
        for file in files:
            st.write("Prévia da planilha: " + file.name)
            if file.name.endswith(".csv"):
                df = pd.read_csv(file)
            else:
                df = pd.read_excel(file)
            st.dataframe(df)

            # text = df.to_string(index=False)
            text = generate_food_beverage_insight(df).to_string()

            analyse(api_key, text, user_question)


def generate_food_beverage_insight(df):
    # Garante que as colunas estão em formato numérico
    df['food'] = pd.to_numeric(df['food'], errors='coerce')
    df['beer'] = pd.to_numeric(df['beer'], errors='coerce')
    df['clothes'] = pd.to_numeric(df['clothes'], errors='coerce')

    # Remove linhas onde os valores são NaN
    df = df.dropna(subset=['food', 'beer', 'month', 'clothes'])

    # Filtro por categorias de interesse
    mask = df['categoria'].str.lower().isin(['food', 'beer', 'clothes'])
    df_filtered = df[mask]

    # Agrupa por mês e soma os valores
    df_filtered['month'] = df_filtered['food'].dt.to_period('month')
    return df_filtered.groupby('month')['value'].sum().sort_values(ascending=False)
