# Module 1 - LangChain Core

---

# Learning Objective

Understand the core building blocks of modern LangChain applications.

By the end of this module, you should understand:

- PromptTemplate
- ChatPromptTemplate
- Chat Models
- Runnables
- LCEL
- Output Parsers
- Structured Outputs
- RunnablePassthrough

---

# 1. Why LangChain Exists

As AI applications grow, developers need:

- Reusable prompts
- Structured workflows
- Tool integration
- Retrieval systems
- Memory management
- Output validation

Without LangChain, applications become difficult to maintain.

---

## Without LangChain

```python
prompt = f"Explain {topic}"

response = model.generate(prompt)
```

Works for simple scripts.

Becomes difficult to manage in large applications.

---

## With LangChain

```python
template = PromptTemplate.from_template(
    "Explain {topic}"
)
```

Prompts become reusable components.

---

# 2. PromptTemplate

## What Is It?

A reusable prompt containing variables.

Example:

```python
template = PromptTemplate.from_template(
    "Explain {topic} to a beginner."
)
```

---

## Invoke

```python
template.invoke({
    "topic": "Machine Learning"
})
```

Output:

```text
Explain Machine Learning to a beginner.
```

---

## Input

```python
dict
```

Example:

```python
{
    "topic": "Machine Learning"
}
```

---

## Output

```text
Prompt String
```

---

## Important

PromptTemplate:

- Does NOT call an LLM
- Does NOT require an API key
- Only generates prompts

---

## Missing Variables

Example:

```python
template = PromptTemplate.from_template(
    "Explain {topic} using {example_type}"
)
```

```python
template.invoke({
    "topic": "Machine Learning"
})
```

Result:

```text
Error
```

LangChain follows:

```text
Fail Fast
```

instead of:

```text
Fail Silently
```

---

# 3. ChatPromptTemplate

## Problem

PromptTemplate creates a single text string.

Modern LLM applications use messages.

---

## Example

```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a Data Science mentor."),
    ("human", "Explain {topic}.")
])
```

---

## Output

```python
[
    SystemMessage(...),
    HumanMessage(...)
]
```

---

## Why Use It?

Provides structure.

Separates:

- System Instructions
- User Requests
- AI Responses

---

## Industry Usage

Most modern applications use:

```python
ChatPromptTemplate
```

instead of:

```python
PromptTemplate
```

because modern models are chat-oriented.

---

# 4. Message Types

---

## SystemMessage

Defines behavior.

Example:

```text
You are a Data Science mentor.
```

Purpose:

```text
How should the model behave?
```

---

## HumanMessage

Represents user input.

Example:

```text
Explain Machine Learning.
```

Purpose:

```text
What does the user want?
```

---

## AIMessage

Represents assistant responses.

Example:

```text
Machine Learning is...
```

Purpose:

```text
What was previously said?
```

---

# 5. Chat Models

Example:

```python
ChatGoogleGenerativeAI
```

---

## Input

Messages

```python
[
    SystemMessage(...),
    HumanMessage(...)
]
```

---

## Output

```python
AIMessage(...)
```

---

## Important

Chat Models are:

```text
Stateless
```

They do not remember previous API calls.

Memory is managed by the application.

---

# 6. Runnables

## Definition

A Runnable is anything that:

```text
Input
 ↓
Work
 ↓
Output
```

---

## Examples

PromptTemplate

```python
dict → prompt
```

---

ChatPromptTemplate

```python
dict → messages
```

---

Model

```python
messages → AIMessage
```

---

Parser

```python
AIMessage → structured output
```

---

## Common Interface

Most runnables support:

```python
.invoke()
```

---

# 7. LCEL

LCEL = LangChain Expression Language

Purpose:

Connect runnables together.

---

## Example

```python
chain = prompt | model
```

Flow:

```text
Prompt
 ↓
Model
```

---

## Example

```python
chain = prompt | model | parser
```

Flow:

```text
Prompt
 ↓
Model
 ↓
Parser
```

---

## Benefits

- Cleaner code
- Composable workflows
- Easier maintenance
- Readable pipelines

---

# 8. Data Flow Thinking

Most important LangChain skill:

Always ask:

```text
What goes in?
What comes out?
```

---

Example:

```python
chain = prompt | model
```

Input:

```python
{
    "topic": "Machine Learning"
}
```

↓

Prompt

↓

Messages

↓

Model

↓

AIMessage

---

# 9. Output Parsers

Purpose:

Convert model output into application-friendly formats.

---

## Without Parser

Output:

```python
AIMessage(...)
```

---

## With StrOutputParser

Output:

```python
str
```

---

Example:

```python
chain = prompt | model | parser
```

---

## Why Use Parsers?

Applications typically need:

- String
- Dictionary
- JSON
- Python Object

instead of AIMessage objects.

---

# 10. StrOutputParser

Purpose:

```python
AIMessage
```

↓

```python
str
```

---

Example

Without parser:

```python
response.content
```

---

With parser:

```python
response
```

already contains text.

---

# 11. Structured Outputs

One of the most valuable LangChain features.

---

## Problem

Model output:

```text
Rahul knows Python and SQL.
```

Hard to process programmatically.

---

## Desired Output

```python
{
    "name": "Rahul",
    "skills": ["Python", "SQL"]
}
```

---

# 12. Pydantic

Pydantic defines schemas.

Example:

```python
class Candidate(BaseModel):
    name: str
    skills: list[str]
    experience_years: int
```

---

## Benefits

- Validation
- Type Safety
- Consistent Outputs

---

# 13. with_structured_output()

Example:

```python
structured_model = model.with_structured_output(
    Candidate
)
```

---

Purpose:

Tell the model to return data matching the schema.

---

## Output

Instead of:

```python
AIMessage(...)
```

You get:

```python
Candidate(...)
```

---

# 14. Structured Output Flow

```text
Candidate Schema
        ↓
LangChain
        ↓
Gemini
        ↓
Structured JSON
        ↓
Pydantic Validation
        ↓
Candidate Object
```

---

## Responsibilities

Gemini:

```text
Extract Information
```

---

LangChain:

```text
Connect Components
```

---

Pydantic:

```text
Validate Structure
```

---

# 15. RunnablePassthrough

Purpose:

Pass input unchanged.

---

Example

```python
RunnablePassthrough().invoke(
    "hello"
)
```

Output:

```python
"hello"
```

---

## Why Useful?

Used heavily in RAG.

Allows original input to continue through a workflow while other components process copies of that input.

---

Example

```python
{
    "context": retriever,
    "question": RunnablePassthrough()
}
```

Meaning:

```text
Question
   ├──► Retriever
   └──► Prompt
```

---

# Interview Questions

## What is PromptTemplate?

Reusable prompt structure with placeholders that are populated at runtime.

---

## What is ChatPromptTemplate?

A prompt template that generates structured messages instead of plain text.

---

## What is a Runnable?

A LangChain component that transforms input into output and supports methods such as `.invoke()`.

---

## What is LCEL?

LangChain Expression Language used to compose runnables into workflows.

---

## Why use Output Parsers?

To convert model outputs into application-friendly formats.

---

## What is StrOutputParser?

A parser that converts AIMessage objects into strings.

---

## What is Pydantic?

A Python library for defining, validating, and enforcing data schemas.

---

## What does with_structured_output() do?

It configures a model to return data that conforms to a specified schema.

---

## What is RunnablePassthrough?

A runnable that returns its input unchanged and is commonly used in RAG workflows.

---

# Key Takeaways

1. PromptTemplate generates prompts.
2. ChatPromptTemplate generates messages.
3. Chat Models consume messages.
4. Runnables use `.invoke()`.
5. LCEL connects runnables with `|`.
6. Output Parsers transform model outputs.
7. Pydantic provides validation and structure.
8. Structured outputs are critical for production systems.
9. RunnablePassthrough preserves inputs in workflows.
10. Always understand input and output types.