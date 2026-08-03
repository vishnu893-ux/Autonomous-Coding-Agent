# 🤖 Autonomous Coding Agent

## Overview
The Autonomous Coding Agent is an AI-powered coding assistant developed using Python, Streamlit, and the Google Gemini API. It generates source code from user prompts, explains the generated code, and creates basic documentation.

## Features
- Generate code using AI
- Explain generated code
- Generate project documentation
- Download generated code
- Simple Streamlit interface

## Technologies Used
- Python
- Streamlit
- Google Gemini API
- python-dotenv

## Project Structure

```
app.py
ai_client.py
requirements.txt
README.md
list_models.py
test.py
generated/
```

## Run

Activate the virtual environment first.

### Windows

```bash
.\.venv\Scripts\activate
```

Then run:

```bash
python -m streamlit run app.py
```

## Future Enhancements
- Debug code
- Optimize code
- Multi-language support
- Chat history
