from langchain_openai import ChatOpenAI
from src.rag.retriever import get_retriever

llm = ChatOpenAI(model="gpt-4o-mini")

retriever = get_retriever()

def triage_agent(user_input):
    docs = retriever.invoke(user_input)

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
    Você é um agente de triagem clínica Care Plus.

    Contexto clínico:
    {context}

    Pergunta:
    {user_input}
    """

    response = llm.invoke(prompt)

    return {
        "response": response.content,
        "docs": context
    }
