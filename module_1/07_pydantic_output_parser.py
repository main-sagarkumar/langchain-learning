import os

from dotenv import load_dotenv
from pydantic import BaseModel, Field

from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

class Candidate(BaseModel):
    name: str = Field(description="Candidate name")

    skills: list[str] = Field(
        description="Technical skills"
    )

    experience_years: int = Field(
        description="Years of experience"
    )

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

structured_model = model.with_structured_output(
    Candidate
)

response = structured_model.invoke(
    """
    Rahul Sharma has 5 years of experience.
    He knows Python, SQL and Machine Learning.
    """
)

print(response)
print(type(response))