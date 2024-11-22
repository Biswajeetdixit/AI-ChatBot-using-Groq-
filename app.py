import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A Chatbot with Groq"

# Initialize conversation history if not already in session state
if "conversation_history" not in st.session_state:
    st.session_state["conversation_history"] = []

# Define the prompt template for the chatbot
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant and you are an AI expert. Your name is Friday. Biswajeet Dixit created you."),
        ('user', "Question: {question}")
    ]
)

# Function to generate response using Groq
def generate_response(question, llm, temperature, max_tokens):
    llm = ChatGroq(model_name=llm, api_key=os.getenv('GROQ_API_KEY'))
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question': question})
    return answer

# Title of the app
st.title("AI ChatBot using Groq")

# Select the Open Source model
llm = st.sidebar.selectbox("Select Open Source model", ['llama-3.1-8b-instant', 'gemma2-9b-IT', "mixtral-8*7b-32768", "whisper-large-v3"])

# Input the Groq API Key
api_key = st.text_input("Enter your Groq API key:", type="password")

# Adjust response parameters
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

# Main interface for user input
st.write("Go ahead, ask any question")
user_input = st.text_input("You:")

# If the user inputs a question
if user_input:
    # Store the conversation history in session state
    conversation_history = "\n".join(st.session_state["conversation_history"])
    full_prompt = f"{conversation_history}\nUser: {user_input}\nAI:"

    # Get the response from the model
    response = generate_response(user_input, llm, temperature, max_tokens)

    # Display the response
    st.write(f"**Friday (AI):** {response}")

    # Add the current user input and response to the conversation history
    st.session_state["conversation_history"].append(f"User: {user_input}")
    st.session_state["conversation_history"].append(f"AI: {response}")

else:
    st.write("Please provide an input.")

# Optional: Show the entire conversation history for context
if st.checkbox("Show Conversation History"):
    for i, message in enumerate(st.session_state["conversation_history"]):
        if i % 2 == 0:  # User messages
            st.write(f"**You:** {message}")
        else:  # AI messages
            st.write(f"**Friday:** {message}")


