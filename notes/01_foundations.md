# Module 0 - Foundations

---

# Learning Objective

Understand how modern LLM applications work before introducing LangChain.

By the end of this module, you should understand:

- What an LLM is
- How LLM APIs work
- What Chat Models are
- Message Roles
- Prompt Engineering
- Why LangChain exists

---

# 1. What is an LLM?

LLM stands for Large Language Model.

An LLM is a machine learning model trained on massive amounts of text data.

Its primary capability is predicting the next token based on previous tokens.

Examples:

- Gemini
- GPT
- Claude

---

## Simplified Architecture

```text
Prompt
   ↓
LLM
   ↓
Response
```

Example:

Input:

```text
Explain Machine Learning.
```

Output:

```text
Machine Learning is a subset of AI...
```

---

# 2. LLM vs ChatGPT

Many beginners confuse these.

## LLM

The underlying model.

Examples:

- Gemini
- GPT
- Claude

---

## ChatGPT

An application built on top of an LLM.

ChatGPT contains:

- User Interface
- Conversation Management
- Tools
- Memory
- File Handling
- Safety Systems
- LLM

---

## Analogy

```text
LLM      = Engine

ChatGPT  = Car
```

The engine powers the car, but the car contains much more.

---

# 3. Why API Keys Exist

API keys allow applications to communicate with AI providers.

Purposes:

- Authentication
- Usage Tracking
- Billing
- Permissions

Example:

```python
api_key = os.getenv("GEMINI_API_KEY")
```

---

# 4. First LLM Application

Architecture:

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

print(response.text)
```

---

# 5. Prompt Engineering

Prompt Engineering is the process of designing instructions and context that guide model behavior.

---

## Good Prompt Structure

A strong prompt often includes:

### Role

```text
You are a Data Science mentor.
```

### Audience

```text
Explain to a beginner.
```

### Context

```text
Use cricket examples.
```

### Constraints

```text
Keep it under 100 words.
```

---

## Example

```text
You are a Data Science mentor.

Explain Machine Learning to a beginner using cricket examples.

Keep the explanation under 100 words.
```

---

# 6. Message Roles

Modern chat models use messages instead of one large text string.

---

## System Message

Controls behavior.

Example:

```text
You are a Data Science mentor.
```

Purpose:

```text
How should the model behave?
```

---

## Human Message

Represents the user's request.

Example:

```text
Explain Machine Learning.
```

Purpose:

```text
What does the user want?
```

---

## AI Message

Represents previous assistant responses.

Example:

```text
Machine Learning is a subset of AI...
```

Purpose:

```text
What did the assistant previously say?
```

---

# 7. Chat Models

Modern AI applications usually use Chat Models.

Examples:

- ChatGoogleGenerativeAI
- ChatOpenAI

---

## Key Idea

Chat Models work with messages.

Input:

```python
[
    SystemMessage(...),
    HumanMessage(...)
]
```

Output:

```python
AIMessage(...)
```

---

## Why Chat Models?

They provide structured conversations.

Instead of:

```text
One Giant String
```

we have:

```text
System Messages
Human Messages
AI Messages
```

This is easier to manage.

---

# 8. Important Misconception

Chat Models do NOT have memory.

LLMs do NOT have memory between API calls.

---

## Wrong Assumption

```text
Chat Model
      ↓
Stores History
```

---

## Reality

```text
Application
      ↓
Stores History
      ↓
Sends History To Model
```

---

# 9. How Chat History Works

Suppose:

```text
User: My name is Sagar

Assistant: Nice to meet you

User: What is my name?
```

Application sends:

```python
[
    HumanMessage("My name is Sagar"),
    AIMessage("Nice to meet you"),
    HumanMessage("What is my name?")
]
```

The model sees the history because the application sends it again.

---

# 10. Why LangChain Exists

Without LangChain:

- Prompt management becomes difficult
- Tool integration becomes difficult
- Memory management becomes difficult
- Retrieval becomes difficult

As applications grow, code becomes harder to maintain.

LangChain provides reusable abstractions for building AI applications.

---

# Key Takeaways

1. LLMs generate text.
2. ChatGPT is an application built on top of an LLM.
3. API keys provide authentication and billing.
4. Prompt quality strongly influences output quality.
5. Chat Models use structured messages.
6. System Messages define behavior.
7. Human Messages contain user requests.
8. AI Messages contain previous assistant responses.
9. Chat Models are stateless.
10. Memory is managed by the application.
11. LangChain exists to simplify AI application development.

---

# Interview Questions

## What is an LLM?

A Large Language Model trained on massive text datasets that generates text by predicting the next token.

---

## What is the difference between an LLM and ChatGPT?

An LLM is the underlying model, while ChatGPT is an application built on top of an LLM with UI, memory, tools, and conversation management.

---

## Why do API keys exist?

Authentication, usage tracking, permissions, and billing.

---

## What is Prompt Engineering?

The process of designing instructions, context, constraints, and examples to guide model behavior.

---

## What are System, Human, and AI Messages?

System Message → behavior instructions

Human Message → user request

AI Message → previous assistant response

---

## Do Chat Models Have Memory?

No.

Chat Models are stateless.

Memory is managed by the application.