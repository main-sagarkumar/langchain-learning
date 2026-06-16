import os
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a Data Science mentor."),
    ("human", "Explain {topic} in 3 bullet points.")
])

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

parser = StrOutputParser()

chain = prompt | model | parser

response = chain.invoke({
    "topic": "Machine Learning"
})

print(type(response))
print(response)
