
from langchain_openai import ChatOpenAI
from src.tools.medication_tools import (
    check_medication_interaction
)

llm = ChatOpenAI(model="gpt-4o-mini")

def prescription_agent(user_input):
    interaction = check_medication_interaction(
        "ibuprofeno"
    )

    prompt = f"""
    Você é um agente de prescrição.

    Interação medicamentosa:
    {interaction}

    Pergunta:
    {user_input}
    """

    response = llm.invoke(prompt)

    return response.content

log_run(state)
return state
