import ollama

response = ollama.chat(
    model="qwen2.5:3b",
    messages=[
        {
            "role": "user",
            "content": "Explain what an AI Agent is in one short paragraph."
        }
    ],
)

print(response["message"]["content"])