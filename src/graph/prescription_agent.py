import logging

logger = logging.getLogger(__name__)

logger.info("SupervisorAgent acionado")

from langchain_ollama import ChatOllama

llm = ChatOpenAI(model="gpt-4o-mini")

def prescription_agent(state):

    response = llm.invoke(f"""
Você é um agente de prescrição.

Paciente: {state['patient']}
Pedido: {state['input']}
""")

    state["final_answer"] = response.content
    state["tools_used"].append("prescription")

    return state
