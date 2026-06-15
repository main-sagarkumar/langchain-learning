# LangChain Learning Journey

This repository contains my hands-on learning journey from LangChain beginner to production-ready AI Engineer.

The goal is to understand not only LangChain APIs, but also the underlying concepts used in modern AI applications such as RAG, Agents, LangGraph, and Production AI Systems.

---

# Learning Roadmap

## Phase 0: Foundations

- LLM Basics
- API Calls
- Prompts
- Chat Models
- Message Roles
- LangChain Motivation

## Phase 1: Core LangChain

- PromptTemplate
- ChatPromptTemplate
- Runnables
- LCEL
- Output Parsers

## Future Phases

- RAG
- Vector Databases
- Agents
- LangGraph
- Production Systems
- Deployment

---

# Module 0 - Foundations

## What is an LLM?

LLM (Large Language Model) is the core AI model responsible for generating text.

Examples:

- Gemini
- GPT
- Claude

An LLM receives input text and predicts the next tokens to generate a response.

---

## LLM vs ChatGPT

### LLM

The model itself.

```text
Input Text
     ↓
LLM
     ↓
Output Text
```

### ChatGPT

An application built on top of an LLM.

```text
UI
Memory
Tools
Safety Layers
Conversation History
        +
LLM
```

ChatGPT is not the model itself.

---

## Why API Keys Exist

API keys are used for:

- Authentication
- Usage Tracking
- Billing
- Permissions

Applications use API keys to communicate with AI providers.

---

## First LLM Application

Flow:

```text
Python Script
      ↓
Gemini API
      ↓
Gemini Model
      ↓
Response
```

Example:

```python
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain Machine Learning."
)
```

---

# Prompt Engineering

Prompt Engineering is the process of designing instructions, context, constraints, examples, and output formats to guide model behavior.

A good prompt usually includes:

- Role
- Context
- Audience
- Desired Output Format

Example:

```text
You are a Data Science mentor.

Explain Machine Learning to a 12-year-old student using cricket examples.
```

---

# Message Roles

Modern chat models work with messages.

## System Message

Controls model behavior.

Example:

```text
You are a Data Science mentor.
```

---

## Human Message

Represents the user's request.

Example:

```text
Explain Machine Learning.
```

---

## AI Message

Represents previous assistant responses.

Example:

```text
Machine Learning is a subset of AI.
```

---

# Chat History

Chat models are stateless.

They do NOT remember previous API calls.

Memory is managed by the application.

The application sends previous messages again on each request.

Example:

```python
[
    HumanMessage("My name is Sagar"),
    AIMessage("Nice to meet you"),
    HumanMessage("What is my name?")
]
```

---

# Module 1 - LangChain Fundamentals

## Why LangChain Exists

Without LangChain:

- Prompt management becomes messy
- Tool integration becomes difficult
- Retrieval becomes difficult
- Memory becomes difficult

LangChain provides reusable components for building AI applications.

---

# PromptTemplate

## Purpose

Create reusable prompts with variables.

Example:

```python
template = PromptTemplate.from_template(
    "Explain {topic} to a beginner."
)
```

Invoke:

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

## Important Notes

PromptTemplate:

- Is NOT an LLM
- Does NOT call Gemini
- Only generates prompts

Input:

```python
dict
```

Output:

```python
Prompt
```

---

# ChatPromptTemplate

Purpose:

Create structured chat messages.

Example:

```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a Data Science mentor."),
    ("human", "Explain {topic}.")
])
```

Output:

```python
[
    SystemMessage(...),
    HumanMessage(...)
]
```

---

## Why Use ChatPromptTemplate?

Modern AI systems are conversational.

ChatPromptTemplate allows:

- System Instructions
- User Messages
- Conversation History
- AI Messages

to be handled in a structured way.

---

# Runnables

A Runnable is anything that:

```text
Input
  ↓
Work
  ↓
Output
```

Examples:

- PromptTemplate
- ChatPromptTemplate
- Chat Models
- Output Parsers

All support:

```python
.invoke()
```

---

# LCEL

LCEL = LangChain Expression Language

Purpose:

Connect Runnables together.

Example:

```python
chain = prompt | model
```

Flow:

```text
Prompt
   ↓
Model
```

More advanced:

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

# Data Flow Understanding

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

ChatPromptTemplate

↓

```python
[
    SystemMessage(...),
    HumanMessage(...)
]
```

↓

Model

↓

```python
AIMessage(...)
```

---

# Important LangChain Principle

Always ask:

```text
What is the input?
What is the output?
```

for every component.

Understanding data flow is more important than memorizing APIs.

---

# Key Takeaways

1. LLMs are the core models.
2. ChatGPT is an application built on top of an LLM.
3. Chat models work with messages.
4. Chat models do not have memory.
5. Memory is managed by the application.
6. PromptTemplate creates prompts.
7. ChatPromptTemplate creates messages.
8. Runnables use `.invoke()`.
9. LCEL connects Runnables using `|`.
10. Always understand input and output types.