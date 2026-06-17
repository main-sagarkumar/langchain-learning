from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

# Load PDF
loader = PyPDFLoader(
    "data/employee_handbook.pdf"
)

documents = loader.load()

# Chunk
splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150
)

chunks = splitter.split_documents(
    documents
)

# Embedding Model
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
)

# Generate one embedding
vector = embeddings.embed_query(
    chunks[0].page_content
)

print(type(vector))
print(len(vector))
print(vector[:10])