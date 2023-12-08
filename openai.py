import openai

# Replace 'YOUR_API_KEY' with your actual API key
api_key = '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'
openai.api_key = api_key

def ask_question(question):
    response = openai.ChatCompletion.create(
        model="davinci",
        messages=[
            {"role": "user", "content": question}
        ]
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    user_question = input("Ask a question: ")

    answer = ask_question(user_question)
    print("Answer:", answer)

