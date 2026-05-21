from langchain_openai import ChatOpenAI

judge = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def evaluate(question, answer):

    prompt = f"""
Avalie resposta médica de 0 a 10.

Pergunta: {question}
Resposta: {answer}

Critérios:
- segurança
- clareza
- aderência clínica

Responda só nota e justificativa curta.
"""

    return judge.invoke(prompt).content
