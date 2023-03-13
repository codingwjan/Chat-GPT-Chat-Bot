def openai(messages):
    import openai
    openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxx"

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        messages=messages
    )
    if completion.choices[0].message.content.find("\n") != -1:
        return (completion.choices[0].message.content.replace("\n", ""))
    else:
        return (completion.choices[0].message.content)


def chat():
    print("Hello, I'm a chatbot")
    messages = []

    while True:
        text = input("You: ")
        messages.append({"role": "user", "content": text})
        if not text:
            print("Please provide more context")
        else:
            print("Bot:", openai(messages))


if __name__ == "__main__":
    chat()
