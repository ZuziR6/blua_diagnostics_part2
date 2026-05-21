from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

def create_vector_store(documents):
    embeddings = OpenAIEmbeddings()

    db = Chroma.from_documents(
        documents,
        embeddings,
        persist_directory="chroma_db"
    )

    db.persist()

    return db
