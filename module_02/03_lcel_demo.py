# LangChain Expression Language (LCEL)
# which lets us compose runnables. (.invoke). Using the pipe operator: |

import os
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

template = PromptTemplate.from_template(
    """
    Explain {topic} to a beginner.
    In 100 words.
    """
)

chain = template | model

topic = input("What you want to learn?: ")

response = chain.invoke({
    "topic": topic
})

print(response.content)
