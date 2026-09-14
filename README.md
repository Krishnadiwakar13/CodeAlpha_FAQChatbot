# 🤖 CodeAlpha FAQ Chatbot

An AI-powered FAQ chatbot built as part of the **CodeAlpha Artificial Intelligence Internship — Task 2**.

The project combines NLP-based FAQ retrieval with a Groq-hosted LLM to provide natural and grounded responses to user questions.

## 📌 Project Overview

This chatbot allows users to ask questions about a predefined set of frequently asked questions.

Instead of sending every question directly to an LLM, the application first searches the FAQ knowledge base using **TF-IDF and cosine similarity**. If a relevant FAQ is found, its information is provided to the LLM to generate a natural response.

This retrieval-first approach helps keep responses grounded in the available FAQ information and reduces the chance of unrelated or unsupported answers.

## ✨ Features

- 💬 Interactive Streamlit chat interface
- 🧠 NLP-based FAQ retrieval
- 🔎 TF-IDF vectorization
- 📊 Cosine similarity matching
- 🔄 Support for different ways of asking the same question
- 🤖 Groq LLM integration
- 🛡️ Similarity threshold for unknown questions
- 🚫 Prevents unrelated questions from being sent to the LLM
- 💾 Conversation history during the session
- 🗑️ Clear chat functionality
- 🔐 API key stored securely using environment variables

## 🧠 How It Works

The chatbot follows a retrieval-first approach:

```text
User Question
      ↓
Text Preprocessing
      ↓
TF-IDF Vectorization
      ↓
Cosine Similarity
      ↓
Find Best Matching FAQ
      ↓
Similarity Threshold
      ↓
Relevant FAQ
      ↓
Groq LLM
      ↓
Natural Language Response
```

If the question does not have a sufficiently relevant FAQ match, the chatbot does not send the question to the LLM. Instead, it informs the user that the required information is not available in the FAQ knowledge base.

## 🔍 FAQ Retrieval

The FAQ system uses **TF-IDF** to represent questions as numerical vectors and **cosine similarity** to determine how closely a user's question matches the stored FAQs.

Each FAQ can contain multiple question variations.

For example:

```text
Main FAQ:
How long does delivery take?

Variations:
- When will my package arrive?
- When should I expect my order?
- How long until my order arrives?
- When will my order be delivered?
```

This allows the system to handle different natural ways of asking the same question.

## 🤖 LLM Integration

After retrieving the most relevant FAQ, the FAQ question and answer are provided as context to a Groq-hosted LLM.

The LLM is instructed to:

- Use only the retrieved FAQ information
- Avoid making assumptions
- Avoid adding unsupported facts
- Keep responses concise and natural
- Not answer questions outside the provided FAQ context

The LLM is therefore used primarily for **natural-language response generation**, while FAQ retrieval and relevance checking are handled by the application's NLP pipeline.

## 🛠️ Technologies Used

- **Python**
- **Streamlit** — Web interface
- **scikit-learn** — TF-IDF and cosine similarity
- **Groq API** — LLM response generation
- **python-dotenv** — Environment variable management
- **JSON** — FAQ knowledge base

## 📁 Project Structure

```text
CodeAlpha_FAQChatbot/
│
├── data/
│   └── faqs.json
│
├── src/
│   ├── __init__.py
│   ├── llm.py
│   └── retriever.py
│
├── tests/
│   ├── __init__.py
│   ├── test_llm.py
│   └── test_retriever.py
│
├── .gitignore
├── app.py
├── requirements.txt
└── README.md
```

> `.env`, `venv`, and Python cache files are excluded from version control through `.gitignore`.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Krishnadiwakar13/CodeAlpha_FAQChatbot.git
cd CodeAlpha_FAQChatbot
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\activate
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

## 🔑 Groq API Configuration

The chatbot uses a Groq API key for LLM response generation.

Create a `.env` file in the project root:

```text
GROQ_API_KEY=your_api_key_here
```

Do not commit the `.env` file to GitHub.

The project includes `.env` in `.gitignore` to help prevent accidental exposure of the API key.

## ▶️ Run the Application

Start the Streamlit application:

```powershell
streamlit run app.py
```

Streamlit will provide a local URL where the chatbot can be opened in a browser.

## 🧪 Testing

The project contains separate tests for the FAQ retrieval and LLM components.

### Test FAQ Retrieval

```powershell
python -m tests.test_retriever
```

The retrieval tests verify questions such as:

```text
When will my package arrive?
I want to send something back
Can I get my money back?
I forgot my password
My order came damaged
```

### Test LLM Integration

```powershell
python -m tests.test_llm
```

This verifies that the Groq integration can generate a response using the supplied FAQ context.

## 💬 Example Questions

The chatbot can handle questions such as:

```text
When will my package arrive?
```

```text
I want to send something back
```

```text
Can I get my money back?
```

```text
I forgot my password
```

```text
Can I pay using UPI?
```

```text
My order came damaged
```

It can also handle different variations of the same question through the FAQ variation system.

## 🚫 Handling Unknown Questions

The chatbot includes a similarity threshold to prevent irrelevant questions from being treated as valid FAQ queries.

For example:

```text
User:
What is the weather today?
```

If no relevant FAQ is found, the application responds that the information is not available in the FAQ knowledge base.

The question is not sent to the LLM in this case.

This retrieval-first approach helps reduce hallucinated answers.

## 🔐 Security

The Groq API key is loaded from an environment variable rather than being written directly in the source code.

The following are excluded from Git:

```text
.env
venv/
__pycache__/
```

Never publish your API key in source code, screenshots, README files, or GitHub commits.

## ⚠️ Limitations

- The chatbot can only answer questions covered by its FAQ knowledge base.
- TF-IDF is based primarily on lexical similarity and may not understand every semantic relationship between words.
- The quality of responses depends on the quality and coverage of the FAQ dataset.
- LLM responses require an internet connection and a valid Groq API key.

## 🚀 Future Improvements

Possible improvements include:

- Expanding the FAQ knowledge base
- Using semantic embeddings for better question matching
- Adding multilingual FAQ support
- Adding voice input and text-to-speech
- Adding persistent conversation storage
- Adding an administrator interface for managing FAQs
- Adding analytics for frequently asked questions
- Deploying the chatbot as a public web application

## 📚 CodeAlpha Internship

This project was developed as part of the:

**CodeAlpha Artificial Intelligence Internship**

**Task:** Task 2 — Chatbot for FAQs

The implementation follows the core requirements of the task by using:

- FAQ data
- Text preprocessing
- Similarity-based matching
- Cosine similarity
- A chatbot interface
- AI-generated natural-language responses

## 👨‍💻 Author

**Krishna Diwakar** 

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in krishna-diwakar-981367305/)

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Krishnadiwakar13)

Built as part of the CodeAlpha AI Internship.

---

⭐ If you find this project useful, consider giving the repository a star.
