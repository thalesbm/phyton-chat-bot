import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_community.chat_models import ChatOpenAI

def analyse(api_key, text, user_question):
    # break it into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n"],
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )

    chunks = text_splitter.split_text(text)
    # st.write(chunks)

    # generating embeddings
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)

    # creating vector store FAISS
    vector_store = FAISS.from_texts(chunks, embeddings)

    # do similarity search
    if user_question:
        match = vector_store.similarity_search(user_question)
        # st.write(match)

        # define llm
        llm = ChatOpenAI(
            openai_api_key=api_key,
            temperature=0,
            max_tokens=1000,
            model_name="gpt-3.5-turbo"
        )

        # output results
        chain = load_qa_chain(llm, chain_type="stuff")
        response = chain.run(
            question=user_question,
            input_documents=match,
        )

        st.write(response)