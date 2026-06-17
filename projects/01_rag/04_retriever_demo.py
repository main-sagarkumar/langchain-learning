from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()

# Load PDF
loader = PyPDFLoader(
    "data/employee_handbook.pdf"
)

documents = loader.load()

# Chunk
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=150
)

chunks = splitter.split_documents(documents)

# Embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

# Chroma
vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

# Retriever
retriever = vector_store.as_retriever()

# Search
results = retriever.invoke(
    "What is the vacation policy?"
)

print(f"Results Found: {len(results)}")

print("\nFirst Result:\n")
print(results[0].page_content)

print("\nMetadata:\n")
print(results[0].metadata)