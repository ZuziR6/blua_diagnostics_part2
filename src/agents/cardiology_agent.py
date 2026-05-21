from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0.2
)

CARDIOLOGY_KEYWORDS = [
    "dor no peito",
    "pressão alta",
    "hipertensão",
    "taquicardia",
    "palpitação"
]


def cardiology_agent(state):

    question = state["question"]

    prompt = f"""
Você é um cardiologista da Care Plus.

Analise os sintomas abaixo:

{question}

Forneça:
- risco cardiovascular
- possíveis causas
- orientação segura
"""

    response = llm.invoke(prompt)

    state["cardiology_response"] = response.content
    state["agent_path"].append("cardiology_agent")

    return state
