from ai_client import generate_code

prompt = "Write a Python program to print Hello World."

result = generate_code(prompt)

print("========== RESULT ==========")
print(repr(result))
print("============================")