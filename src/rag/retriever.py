from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

def get_retriever():
    db = Chroma(
        persist_directory="chroma_db",
        embedding_function=OpenAIEmbeddings()
    )

    return db.as_retriever(search_kwargs={"k": 3})
