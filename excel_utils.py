import streamlit as st
import pandas as pd
from main_logic import analyse

def readExcel(api_key):
    # upload documents
    st.header("Chat para analisar documentos")

    with st.sidebar:
        st.title("Documentos")
        file = st.file_uploader("Anexar arquivos Excel", type=["xlsx", "xls", "csv"])

    # get user question
    user_question = st.text_input("Digite sua pergunta")

    if file is None:
        st.write("arquivo não encontrado")

    if file is not None:
        df = pd.read_csv(file)
        st.write("Prévia da planilha:")
        st.dataframe(df)

        text = df.to_string(index=False)

        analyse(api_key, text, user_question)
