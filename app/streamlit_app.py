import streamlit as st
from src.graph.workflow import graph

st.title("BluaDiagnostics - Care Plus")

user_input = st.text_input(
    "Digite seus sintomas:"
)

if st.button("Enviar"):

    result = graph.invoke({
        "input": user_input
    })

    st.write(result)

    if "docs" in result:
        st.subheader("Documentos recuperados pelo RAG")
        st.write(result["docs"])


st.write(result["agent_path"])
st.write(result["rag_docs"])
