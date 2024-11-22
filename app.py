import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Ensure the API key is loaded from the environment or raise an error
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    st.error("GROQ_API_KEY is not set. Please provide it in the .env file or input it below.")
    groq_api_key = st.text_input("Enter your Groq API key:", type="password")
    if groq_api_key:
        os.environ["GROQ_API_KEY"] = groq_api_key
        st.success("API key has been set.")
else:
    st.success("API key loaded from environment.")

# LangChain Tracking Settings
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACKING_V2'] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A Chatbot with Groq"

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant and an AI expert. Your name is Friday. Biswajeet Dixit created you."),
        ('user', "Question: {question}")
    ]
)

# Function to generate responses
def generate_response(question, llm, temperature, max_tokens):
    llm = ChatGroq(model_name=llm, api_key=groq_api_key)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question': question})
    return answer

# Title of the app
st.title("AI ChatBot using Groq")

# Sidebar for model selection
llm = st.sidebar.selectbox("Select Open Source model", ['llama-3.1-8b-instant', 'gemma2-9b-IT', "mixtral-8*7b-32768", "whisper-large-v3"])

# Adjust response parameters
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

# Main interface for user input
st.write("Go ahead, ask any question:")
user_input = st.text_input("You:")

# Display the response if a question is entered
if user_input:
    response = generate_response(user_input, llm, temperature, max_tokens)
    st.write(response)
else:
    st.write("Please provide an input.")




