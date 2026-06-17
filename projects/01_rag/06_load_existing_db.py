from dotenv import load_dotenv

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# Same embedding model used during indexing
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

# Load existing Chroma DB
vector_store = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)

retriever = vector_store.as_retriever()

prompt = ChatPromptTemplate.from_template(
    """
    Answer the question using ONLY the provided context.

    Include ALL relevant details found in the context.

    Do not summarize or omit information.

    Present the answer as bullet points.
    
    If the answer is not present in the context,
    say "I could not find that information."

    Context:
    {context}

    Question:
    {question}
    """
)


model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser = StrOutputParser()

chain = (
    {
        "context": retriever,
        "question": RunnablePassthrough()
    }
    | prompt
    | model
    | parser
)

response = chain.invoke("What is the vacation policy?")

print(response)