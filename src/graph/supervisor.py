from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def supervisor(state):
    prompt = f"""
Classifique em: triage, prescription, escalation, out_of_scope

Paciente: {state['patient']}
Sintomas: {state['input']}

Responda só a classe.
"""
    route = llm.invoke(prompt).content.strip().lower()
    state["route"] = route
    return state
