import openai

openai.api_key = "sk-proj-B39jmSjnRdYpnUAGeOECT3BlbkFJOzbjWZB7x7zgBgDBRWru"

def chat_with_yone(prompt, chat_history):
    chat_history.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=chat_history
    )
    
    reply = response.choices[0].message.content.strip()
    chat_history.append({"role": "assistant", "content": reply})
    return reply

if __name__ == '__main__':
    chat_history = []
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_yone(user_input, chat_history)
        print("Yone: ", response)
