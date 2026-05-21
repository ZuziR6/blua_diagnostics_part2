import os
from langchain_core.tools import tool
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

# Aponta para onde o banco Chroma foi persistido
CHROMA_DIR = os.path.join(os.getcwd(), "data", "chroma_db")
embeddings = OpenAIEmbeddings()
db = Chroma(persist_directory=CHROMA_DIR, embedding_function=embeddings)
retriever = db.as_retriever(search_kwargs={"k": 3})

@tool
def consultar_base_conhecimento(query: str) -> str:
    """Consulte as diretrizes clínicas da Blua Diagnostics sobre sintomas e protocolos."""
    docs = retriever.invoke(query)
    return "\n\n".join([doc.page_content for doc in docs])

@tool
def buscar_prontuario_paciente(cpf: str) -> dict:
    """Busca o histórico clínico simulado do paciente na base Care Plus."""
    # Retorno fixo obrigatório da especificação da Sprint:
    return {
        "nome": "Maria", 
        "idade": 34, 
        "historico": "Hipertensão", 
        "ultima_consulta": "03/2026 com Dr. João", 
        "medicacao_continua": "Losartana 50mg"
    }
