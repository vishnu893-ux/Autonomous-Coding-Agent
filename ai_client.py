import os
from dotenv import load_dotenv
from google import genai
import time

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_code(prompt):
    final_prompt = f"""
You are an Autonomous Coding Agent.

Generate clean and correct code only.
Do not use markdown.
Do not explain unless asked.

User Request:
{prompt}
"""

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-flash-latest",
                contents=final_prompt
            )
            return response.text

        except Exception as e:
            if "503" in str(e):
                time.sleep(3)
                continue
            return f"Error: {e}"

    return "Gemini servers are busy. Please try again in a minute."

def explain_code(code):
    try:
        prompt = f"""
You are an expert programming tutor.

Explain the following code in simple English.

Code:
{code}
"""

        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error: {e}"

def generate_documentation(code):
    try:
        prompt = f"""
You are an expert technical writer.

Generate professional documentation for the following code.

Include:
1. Project Title
2. Description
3. Features
4. Requirements
5. Usage
6. Expected Output

Code:
{code}
"""

        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )

        return response.text

    except Exception as e:
        if "503" in str(e):
            return "Gemini server is busy. Please try again in a few seconds."
        return f"Error: {e}"