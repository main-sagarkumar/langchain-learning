import os
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a Data Science mentor."),
    ("human", "Explain {topic} in 3 bullet points.")
])

chain = prompt | model

response = chain.invoke({
    "topic": "Machine Learning",
    "example_type": "cricket"
})

print(response.content)
