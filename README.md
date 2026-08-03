# 🤖 Autonomous Coding Agent

An AI-powered coding assistant built using **Python**, **Streamlit**, and the **Google Gemini API**. This application helps users generate source code, understand code through explanations, and automatically create project documentation from natural language prompts.

---

## 📌 Overview

The Autonomous Coding Agent is designed to simplify the software development process by leveraging Generative AI. Users can enter a programming request, choose a programming language, and instantly receive AI-generated code. The application also provides code explanations and generates documentation, making it useful for students, beginners, and developers.

---

## ✨ Features

- 🚀 Generate source code from text prompts
- 💻 Supports multiple programming languages
- 📖 Explain generated code in simple language
- 📝 Generate project documentation automatically
- 📥 Download generated code
- 🎨 User-friendly Streamlit interface
- 🤖 Powered by Google Gemini AI

---

## 🛠️ Technologies Used

- Python 3.14
- Streamlit
- Google Gemini API
- python-dotenv

---

## 📂 Project Structure

```
Autonomous-Coding-Agent/
│
├── app.py
├── ai_client.py
├── list_models.py
├── test.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── generated/
│   ├── generated_code.py
│   └── documentation.md
│
└── assets/
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/<username>/Autonomous-Coding-Agent.git
```

### Move into the project directory

```bash
cd Autonomous-Coding-Agent
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment (Windows)

```bash
.\.venv\Scripts\activate
```

### Install the required packages

```bash
python -m pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Get your API key from:

https://aistudio.google.com/app/apikey

---

## ▶️ Run the Application

After activating the virtual environment, start the application using:

```bash
python -m streamlit run app.py
```

The application will open automatically in your default browser.

---

## 📷 Sample Workflow

1. Select a programming language.
2. Enter a coding prompt.
3. Click **Generate Code**.
4. View the generated code.
5. Generate an explanation if required.
6. Generate documentation.
7. Download the generated code.

---

## 🚀 Future Enhancements

- AI-based code debugging
- Code optimization suggestions
- Chat history
- Multiple AI model support
- Dark mode interface
- Voice-based prompt input

---



This project was developed for educational and internship purposes.
