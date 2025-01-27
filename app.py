import streamlit as st

from langchain_groq import ChatGroq

from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser

import os





import os

from dotenv import load_dotenv

load_dotenv()





## Lang_Chain Tracking


os.environ["LANGCHAIN_PROJECT"]="Simple Q&A Chatbot with Groq"





#prompt template

prompt=ChatPromptTemplate.from_messages(

    [

        ("system","You are a heplfull assistant and you are a AI expert your name is friday . Biswajeet dixit created you"),

        ('user',"Question:{question}")

    ]

)





def generate_response(question,llm,temprature,max_tokens):

    llm=ChatGroq(model_name='llama-3.3-70b-specdec',api_key=api_key)

    output_parser=StrOutputParser()

    chain=prompt|llm|output_parser

    answar=chain.invoke({'question':question})

    return answar



### Titel_of the app

st.title("AI ChatBot using Groq")







## Select the OpenAI model

llm=st.sidebar.selectbox("Select Open Source model",['llama-3.3-70b-specdec','gemma2-9b-IT',"mixtral-8*7b-32768","whisper-large-v3"])



## Input the Groq API Key

api_key=st.text_input("Enter your Groq API key:",type="password")



## Adjust response parameter

temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)

max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)



       

## Main interface for user input
st.write("Go ahead, ask any question")
user_input = st.text_area("You:", height=150)

if user_input:
    response = generate_response(user_input, api_key, temperature, max_tokens)
    st.write(response)
else:
    st.write("Please provide the input")





