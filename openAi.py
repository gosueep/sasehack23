from db import generate_suggestion

prompt = "What should I say to start a conversation?"
suggestion = generate_suggestion(prompt)
print("Suggestion:", suggestion)

