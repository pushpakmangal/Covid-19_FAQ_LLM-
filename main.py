import streamlit as st
from my_func import get_qa_chain, create_vector_db

st.title("Covid-19 Q&A 🧑‍")

question = st.text_input("Question: ")

if question:
    try:
        chain = get_qa_chain()
        response = chain(question)

        st.header("Answer")
        st.write(response["result"])
    except Exception as e:
        # st.error(f"An error occurred while processing the question: {e}")
        st.write("I don't know")
