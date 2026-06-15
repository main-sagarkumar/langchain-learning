from langchain_core.prompts import PromptTemplate

template = PromptTemplate.from_template(
    "Explain {topic} using {example_type} examples."
)

print(template.input_variables)