import streamlit as st
from PyPDF2 import PdfReader
from logic import analyse

def readPDF(api_key):
    # upload documents
    st.header("Chat para analisar documentos")

    with st.sidebar:
        st.title("Documentos")
        files = st.file_uploader(
            label="Anexar arquivos PDF",
            type="pdf",
            accept_multiple_files=True,
        )

    # get user question
    user_question = st.text_input("Digite sua pergunta")

    # extrct the text
    if files is None:
        st.write("arquivo não encontrado")

    if files is not None:
        text = ""
        for file in files:
            pdf_reader = PdfReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text()

        analyse(api_key, text, user_question)
