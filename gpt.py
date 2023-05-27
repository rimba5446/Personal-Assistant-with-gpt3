import openai

# Set OpenAI API key
openai.api_key = "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"

def chatbot(prompt, history):
     # Prepare the prompt by including the previous conversation history
    prompt = "\n".join(history) + "\n" + prompt
    
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

history = []
print("Hi, I am Raymujan, your personal voice assistant. How can I help you today?")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chatbot(user_input, history)
    history.append("You: " + user_input)
    history.append("Chatbot: " + response)
    print("Chatbot: " + response)
