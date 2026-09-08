# Task 2: System Prompt – Claude Based

## Objective

Work on the **System Prompt – Claude Based** task.

The objective is to understand how a well-designed system prompt can control the **behaviour, role, instructions, and output** of an LLM.

---

## Introduction

Large Language Models (LLMs) such as **Claude, GPT, Gemini, and Llama** generate responses based on instructions provided to them.

One of the most important components that guides an LLM's behaviour is the **system prompt**.

A system prompt is a set of instructions given to the model before any user interaction takes place. It defines the model's:

* Role
* Responsibilities
* Constraints
* Tone
* Behaviour
* Output format

In Claude-based systems, well-designed system prompts help ensure that responses are **accurate, safe, consistent, and aligned with the intended purpose of the application**.

This task explores how system prompts influence the behaviour and performance of LLMs.

---

# 1. What is a System Prompt?

A **system prompt** is a high-level instruction that establishes how an AI assistant should behave throughout a conversation.

It acts as a set of rules that the model follows when responding to user queries.

## Purpose of a System Prompt

A system prompt helps to:

* Define the AI's role.
* Set behavioural guidelines.
* Establish response style and tone.
* Limit unwanted actions.
* Improve consistency and reliability.
* Ensure safe and ethical outputs.

Without a system prompt, the model may generate responses that are **inconsistent, off-topic, or unsuitable** for the intended application.

---

# 2. Importance of System Prompts in Claude

Claude is designed to follow instructions and align its behaviour with the goals specified in the system prompt.

A well-designed prompt helps Claude:

* Produce accurate responses.
* Follow organisational policies.
* Maintain a professional tone.
* Avoid harmful or inappropriate content.
* Format outputs consistently.
* Stay focused on specific tasks.

### Example

A **customer service chatbot** and a **medical information assistant** may use the same underlying model but receive different system prompts to suit their specific roles.

---

# 3. Structure of a Claude-Based System Prompt

A system prompt generally contains the following components:

## A. Role Definition

The prompt specifies **who the AI should act as**.

### Example

> "You are a professional customer support assistant."

This helps the model adopt the correct perspective and behaviour.

---

## B. Behavioural Instructions

The prompt explains **how the assistant should respond**.

### Example

* Be polite and professional.
* Provide concise answers.
* Ask clarifying questions when needed.

These instructions guide the overall interaction style.

---

## C. Task Constraints

The prompt defines **limitations and boundaries**.

### Example

* Do not provide legal advice.
* Do not generate harmful content.
* Do not make up information.

This reduces the risk of inappropriate responses.

---

## D. Output Formatting

Instructions can specify **how responses should be presented**.

### Example

* Use bullet points.
* Provide step-by-step explanations.
* Include a summary section.

This ensures consistency and readability.

---

## E. Safety Requirements

Modern AI systems require safety rules.

### Example

* Refuse dangerous requests.
* Protect user privacy.
* Avoid biased language.

These safeguards help maintain responsible AI use.

---

# 4. Example of a Claude-Based System Prompt

Below is an example of a well-structured system prompt:

```text
You are Claude, an AI learning assistant.

Your responsibilities are:
- Help students understand academic concepts.
- Provide clear and accurate explanations.
- Use simple language where possible.
- Give examples to improve understanding.

Rules:
- Do not provide false information.
- If uncertain, state the limitation clearly.
- Remain respectful and professional.
- Do not generate harmful or inappropriate content.

Formatting:
- Use headings and bullet points.
- Provide concise summaries at the end of explanations.
```

This prompt clearly defines the **role, instructions, limitations, and output structure**.

---

# 5. How System Prompts Control LLM Behaviour

System prompts influence the model in several ways.

## Role Control

The model adapts its responses according to the assigned role.

### Example: Teacher

**Response style:**

* Educational
* Detailed
* Explanatory

### Example: Customer Support Agent

**Response style:**

* Professional
* Solution-focused
* Concise

---

## Tone Control

The system prompt can determine whether responses are:

* Formal
* Friendly
* Professional
* Technical
* Academic

### Example

**Prompt:**

> "Respond in a professional and formal tone."

The model will avoid casual language and slang.

---

## Content Control

The prompt determines what information should or should not be included.

### Example

**Prompt:**

> "Only provide information supported by reliable sources."

This encourages more accurate and trustworthy outputs.

---

## Formatting Control

The model can be instructed to use:

* Bullet points
* Numbered lists
* Tables
* Short paragraphs
* Step-by-step instructions

This improves readability and consistency.

---

# 6. Benefits of Well-Designed System Prompts

A strong system prompt offers several advantages.

## Improved Consistency

Responses remain similar in quality and structure across different interactions.

## Better User Experience

Users receive clear, relevant, and helpful answers.

## Increased Safety

The model is less likely to produce harmful or inappropriate content.

## Reduced Hallucinations

Instructions encouraging factual accuracy help minimise incorrect information.

## Alignment with Organisational Goals

The AI behaves according to company policies and requirements.

---

# 7. Challenges in System Prompt Design

Although system prompts are powerful, there are several challenges.

## Ambiguous Instructions

If instructions are unclear, the model may misinterpret them.

## Conflicting Requirements

Two instructions may conflict with each other, causing inconsistent behaviour.

## Prompt Injection Risks

Users may attempt to override system instructions through carefully crafted inputs.

## Maintenance

Prompts may need regular updates as application requirements change.

---

# 8. Key Learning from the Task

This task highlights that **system prompts are essential for controlling the behaviour of Claude and other LLMs**.

Key lessons include:

* System prompts define the model's role and responsibilities.
* They influence tone, style, accuracy, and output format.
* Well-designed prompts improve consistency and user experience.
* Safety instructions help prevent harmful or inappropriate responses.
* Effective prompt engineering is a critical skill when developing AI applications.

---

# Conclusion

System prompts are a fundamental component of **Claude-based and other LLM-based systems**.

They enable developers to control how the model behaves, communicates, and responds to users.

By defining **roles, behavioural rules, safety guidelines, and formatting requirements**, system prompts ensure that AI systems remain useful, reliable, and aligned with their intended purpose.

Therefore, designing effective system prompts is an important aspect of developing **successful AI applications**.
