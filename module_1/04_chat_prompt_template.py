from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a Data Science mentor."),
    ("human", "Explain {topic} to a beginner.")
])

messages = prompt.invoke({
    "topic": "Machine Learning"
})

print(messages)