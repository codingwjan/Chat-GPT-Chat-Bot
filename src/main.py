def openai(messages):
    import openai
    openai.api_key = "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"

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=1,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        messages=messages
    )
    messages.append({"role": "assistant", "content": completion.choices[0].message.content})
    return (completion.choices[0].message.content)


def chat():
    print("Welcome to the OpenAI GPT-3 chatbot!")
    messages = [
        {"role": 'system', "content":"youre name is jan and you are a developer. you are 18 years old. i am like a human assistant. i am the personal assistant of jan."}
    ]

    while True:
        text = input("You: ")
        messages.append({"role": "user", "content": text})
        if not text:
            print("Please provide more context")
        else:
            print("Bot:", openai(messages))


if __name__ == "__main__":
    chat()
