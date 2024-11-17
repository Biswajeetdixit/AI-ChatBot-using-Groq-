import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()

# Lang_Chain Tracking

os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A Chatbot with Groq"

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant and AI expert. Your name is Friday. Biswajeet Dixit created you."),
        ('user', "Question: {question}")
    ]
)

# Generate response function
def generate_response(question, model_name, api_key, temperature, max_tokens):
    llm = ChatGroq(model_name=model_name, api_key=api_key)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question': question})
    return answer

# Title of the app
st.title("AI ChatBot using Groq")

# Select the model and parameters from the sidebar
model_name = st.sidebar.selectbox("Select Open Source model", 
                                  ['llama-3.1-8b-instant', 'gemma2-9b-IT', "mixtral-8*7b-32768", "whisper-large-v3"])

# Input for the Groq API Key
api_key = st.text_input("Enter your Groq API key:", type="password")

# Adjust response parameters
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

# Main interface for user input
st.write("Go ahead, ask any question.")
user_input = st.text_input("You:")

if user_input and api_key:
    response = generate_response(user_input, model_name, api_key, temperature, max_tokens)
    st.write(response)
elif not api_key:
    st.write("Please enter your Groq API key.")
else:
    st.write("Please provide an input question.")
