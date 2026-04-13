import requests

def chat_with_ollama(prompt):
    # Send the prompt to Ollama's API
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama2", "prompt": prompt},
        stream=True  # stream=True lets us read tokens as they arrive
    )

    full_message = ""
    for line in response.iter_lines():
        if line:
            data = line.decode("utf-8")
            # Each line is a JSON object; extract the "response" field
            if '"response"' in data:
                part = data.split('"response":"')[1].split('"')[0]
                full_message += part
            # Stop when Ollama signals done
            if '"done":true' in data:
                break

    return full_message.strip()

# Simple chat loop
if __name__ == "__main__":
    print("Chat with Ollama (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        reply = chat_with_ollama(user_input)
        print("Ollama:", reply)
