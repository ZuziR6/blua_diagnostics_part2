from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader
from src.rag.vector_store import create_vector_store

loader = DirectoryLoader(
    "data/knowledge_base",
    glob="**/*.md"
)

documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

create_vector_store(chunks)

print("Base vetorial criada.")
