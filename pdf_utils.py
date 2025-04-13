import streamlit as st
from PyPDF2 import PdfReader
from main_logic import analyse

def readPDF(api_key):
    # upload documents
    st.header("Chat para analisar documentos")

    with st.sidebar:
        st.title("Documentos")
        file = st.file_uploader("Anexar arquivos PDF", type="pdf")

    # get user question
    user_question = st.text_input("Digite sua pergunta")

    # extrct the text
    if file is None:
        st.write("arquivo não encontrado")

    if file is not None:
        pdf_reader = PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
            # st.write(text)

        analyse(api_key, text, user_question)