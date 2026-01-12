import streamlit as st
import subprocess
st.title("Gemma Chatbot")

user_input= st.text_input("You: ", "Hello, how are you?")

if user_input:
    result=subprocess.run(["ollama", "run", "gemma", user_input], capture_output=True, text=True)

    st.write("Gemma")
    st.write(result.stdout)
    