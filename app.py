import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A Chatbot with Groq"

# Initialize conversation history in session state
if "conversation_history" not in st.session_state:
    st.session_state["conversation_history"] = []

# Define the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant and an AI expert. Your name is Friday. Biswajeet Dixit created you."),
        ("user", "Question: {question}")
    ]
)

# Function to generate responses and maintain memory
def generate_response(question, model_name, api_key, temperature, max_tokens):
    # Initialize the Groq LLM
    llm = ChatGroq(model_name=model_name, api_key=api_key, temperature=temperature, max_tokens=max_tokens)
    
    # Append conversation history to the prompt
    conversation_context = "\n".join(st.session_state["conversation_history"])
    full_prompt = f"{conversation_context}\nUser: {question}\nAI:"
    
    # Generate response
    response = llm.invoke(full_prompt)
    
    # Update conversation history
    st.session_state["conversation_history"].append(f"User: {question}")
    st.session_state["conversation_history"].append(f"AI: {response}")
    return response

# Streamlit UI
st.title("AI ChatBot using Groq")

# Sidebar options
model_name = st.sidebar.selectbox(
    "Select Open Source model",
    ['llama-3.1-8b-instant', 'gemma2-9b-IT', "mixtral-8*7b-32768", "whisper-large-v3"]
)
api_key = st.text_input("Enter your Groq API key:", type="password")
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

# User input interface
st.write("Go ahead, ask any question:")
user_input = st.text_input("You:")

if user_input:
    # Generate response
    response = generate_response(
        user_input,
        model_name=model_name,
        api_key=api_key,
        temperature=temperature,
        max_tokens=max_tokens
    )
    st.write(f"Friday: {response}")
else:
    st.write("Please provide an input.")

# Display conversation history
if st.checkbox("Show Conversation History"):
    st.write("### Conversation History:")
    for i, message in enumerate(st.session_state["conversation_history"]):
        if i % 2 == 0:  # User messages
            st.write(f"**You:** {message}")
        else:  # AI messages
            st.write(f"**Friday:** {message}")



