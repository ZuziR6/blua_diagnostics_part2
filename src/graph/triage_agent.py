import logging

logger = logging.getLogger(__name__)

logger.info("SupervisorAgent acionado")

from src.rag.retriever import get_retriever
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")
retriever = get_retriever()

def triage_agent(state):

    docs = retriever.invoke(state["input"])
    state["retrieved_docs"] = [d.page_content for d in docs]

    response = llm.invoke(f"""
Paciente: {state['patient']}
Contexto: {state['retrieved_docs']}
Sintomas: {state['input']}
""")

    state["final_answer"] = response.content
    state["tools_used"].append("rag")

    return state
