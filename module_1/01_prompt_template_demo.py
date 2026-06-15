"""
First LangChain PromptTemplate Example
"""

from langchain_core.prompts import PromptTemplate

# Create reusable template
template = PromptTemplate.from_template(
    "Explain {topic} to a beginner in {words} words."
)

# Fill variables
prompt = template.invoke({
    "topic": "Machine Learning",
    "words": 100
})

print(prompt)