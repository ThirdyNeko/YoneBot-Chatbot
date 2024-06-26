import openai
import streamlit as st

openai.api_key = "sk-proj-B39jmSjnRdYpnUAGeOECT3BlbkFJOzbjWZB7x7zgBgDBRWru"

def chat_with_yone(prompt, chat_history):
    chat_history.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=chat_history
    )
    
    reply = response.choices[0].message.content.strip()
    chat_history.append({"role": "assistant", "content": reply})
    return reply, chat_history

# Streamlit app
def main():
    st.title("Chat with Yone")
    st.write("Type a message to start chatting with Yone. Type 'quit', 'exit', or 'bye' to end the chat.")
    
    chat_history = []
    user_input = st.text_input("You:", key="input")
    
    if user_input:
        response, chat_history = chat_with_yone(user_input, chat_history)
        st.text_area("Yone:", value=response, height=100)
        
        # Display the chat history
        st.write("Chat History:")
        for message in chat_history:
            role = "User" if message["role"] == "user" else "Yone"
            st.write(f"{role}: {message['content']}")

if __name__ == '__main__':
    main()
