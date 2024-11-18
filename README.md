# AI-ChatBot-using-Groq-


AI ChatBot using Groq
This project is an AI-powered chatbot application built with Groq's Large Language Models (LLMs) and Streamlit. The chatbot, named "Friday," is designed to answer questions with the expertise of an AI assistant. Created by Biswajeet Dixit, Friday is your helpful assistant for answering questions on various topics, leveraging Groq's advanced LLMs for accurate and engaging responses.

Features
Interactive Chat Interface: The chatbot is deployed using Streamlit, offering a user-friendly and interactive platform.
Model Selection Slider: Choose between multiple open-source LLMs, such as llama-3.1-8b-instant, gemma2-9b-IT, mixtral-8*7b-32768, and whisper-large-v3, via a dropdown slider. Each model has unique strengths, allowing flexibility in response style and accuracy.
Customizable Response Settings:
Temperature: Controls the creativity of responses. A lower temperature (e.g., 0.2) makes the chatbot more focused and deterministic, while a higher temperature (e.g., 0.8) makes it more creative and varied.
Max Tokens: Defines the response length. A lower token limit (e.g., 50) keeps responses short, while a higher limit (e.g., 300) allows for more detailed answers.
Getting Started
Prerequisites
Python: Make sure Python is installed.
Libraries: Install the required Python packages listed in requirements.txt (e.g., langchain, python-dotenv, streamlit, and langchain_groq).
Installation
Clone this repository.
Install dependencies:

pip install -r requirements.txt
Create a .env file with your LANGCHAIN_API_KEY.
Running the App
Run the Streamlit app:

streamlit run app.py
Enter your Groq API key when prompted.
Choose an LLM model from the sidebar, set temperature, and token limit as desired.
Ask any question and let Friday provide AI-driven answers.
Detailed Features
Model Selection Slider
The sidebar provides a slider where users can select from various open-source models. Each model is uniquely optimized for specific tasks:

llama-3.1-8b-instant: Fast and efficient for general-purpose Q&A.
gemma2-9b-IT: Tailored for IT-related questions, providing detailed and accurate responses.
mixtral-8*7b-32768: Capable of handling complex queries across multiple domains.
whisper-large-v3: Effective for language translation and conversational responses.
Temperature Control
Slider Range: 0.0 to 1.0.
Function: Adjusts the creativity of responses.
Low Temperature (e.g., 0.2): Gives more deterministic and precise answers.
High Temperature (e.g., 0.8): Encourages diverse and creative responses.
Max Tokens Limit
Slider Range: 50 to 300.
Function: Controls the length of the response.
Low Token Count (e.g., 50): Generates concise responses.
High Token Count (e.g., 300): Produces more detailed and elaborate answers.
Screenshots
Main Chat Interface

Sidebar Controls
Model Selection, Temperature, and Max Tokens:
Note: Replace ./screenshots/chat_interface.png and ./screenshots/sidebar_settings.png with the actual file paths of your screenshots.

Project Structure
app.py: Main script for the Streamlit chatbot interface.
requirements.txt: Lists all dependencies.
.env: Contains environment variables like LANGCHAIN_API_KEY (not included in the repository for security).
Future Improvements
Expanding model options to support additional LLMs.
Adding context retention for more conversational interactions.
Integrating with additional APIs for extended capabilities.
