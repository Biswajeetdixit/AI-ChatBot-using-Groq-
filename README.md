# AI-ChatBot-using-Groq-

# 🤖 AI ChatBot using Groq 🚀

This project is an AI-powered chatbot application built with Groq's Large Language Models (LLMs) and Streamlit. The chatbot, named **Friday**, is designed to answer questions with the expertise of an AI assistant. Created by **Biswajeet Dixit**, Friday is here to help you with questions on various topics, leveraging Groq's advanced LLMs for accurate and engaging responses.

![Image Alt Text](https://github.com/Biswajeetdixit/AI-ChatBot-using-Groq-/blob/a7dd7b8d57641c75ecf4576ac7b7913dfe8a3719/Screenshot%20(29).png)



---

## ✨ Features
- **Interactive Chat Interface**: The chatbot is deployed using Streamlit, offering a user-friendly and interactive platform.
- **Model Selection Slider**: Choose between multiple open-source LLMs, such as `llama-3.1-8b-instant`, `gemma2-9b-IT`, `mixtral-8*7b-32768`, and `whisper-large-v3`, via a dropdown slider. Each model has unique strengths, allowing flexibility in response style and accuracy.
- **Customizable Response Settings**:
    - **🔥 Temperature**: Controls the creativity of responses. A lower temperature (e.g., 0.2) makes the chatbot more focused and deterministic, while a higher temperature (e.g., 0.8) makes it more creative and varied.
    - **📏 Max Tokens**: Defines the response length. A lower token limit (e.g., 50) keeps responses short, while a higher limit (e.g., 300) allows for more detailed answers.

---

## 🛠️ Getting Started

### 📋 Prerequisites
- **🐍 Python**: Make sure Python is installed.
- **📦 Libraries**: Install the required Python packages listed in `requirements.txt` (e.g., `langchain`, `python-dotenv`, `streamlit`, and `langchain_groq`).

### ⚙️ Installation
1. Clone this repository:
   ```bash
   git clone <repository-url>

Navigate to the project directory:

cd <repository-name>
Install dependencies:

pip install -r requirements.txt
Create a .env file with your LANGCHAIN_API_KEY.



## 🚀 Running the App

1. **Start the Streamlit app:**
   
   streamlit run app.py
# Enter your 🔑 Groq API key when prompted.
# Select an LLM model from the sidebar, and adjust Temperature and Max Tokens as desired.
# Ask any question and let Friday provide AI-driven answers!
![AI Model Diagram](https://github.com/Biswajeetdixit/AI-ChatBot-using-Groq-/blob/886a9658e9ef7c45f26332a558b8167753265705/Screen_short%26Video/Groq_llama%20.png)


## 💡 Detailed Features

### 🎛️ Model Selection Slider
The sidebar provides a slider where users can select from various open-source models. Each model is uniquely optimized for specific tasks:
- **llama-3.1-8b-instant**: Fast and efficient for general-purpose Q&A.
- **gemma2-9b-IT**: Tailored for IT-related questions, providing detailed and accurate responses.
- **mixtral-8*7b-32768**: Capable of handling complex queries across multiple domains.
- **whisper-large-v3**: Effective for language translation and conversational responses.

### 🔥 Temperature Control
Slider Range: 0.0 to 1.0.
Function: Adjusts the creativity of responses.
- **Low Temperature (e.g., 0.2)**: Gives more deterministic and precise answers.
- **High Temperature (e.g., 0.8)**: Encourages diverse and creative responses.

### ✏️ Max Tokens Limit
Slider Range: 50 to 300.
Function: Controls the length of the response.
- **Low Token Count (e.g., 50)**: Generates concise responses.
- **High Token Count (e.g., 300)**: Produces more detailed and elaborate answers.

---

## 📸 Screenshots & Demo

Here’s a quick look at the interface!

- **🖼️ Main Chat Interface**
- **🖼️ Sidebar Controls**: Model Selection, Temperature, and Max Tokens:

### 🎞️ Demo GIF
You can use a GIF (like one generated by ScreenToGif or a similar tool) to show:
- Entering the API key.
- Choosing a model.
- Adjusting temperature and max tokens.
- Asking a question and viewing the response from Friday.

---

## 🗂️ Project Structure

- **app.py**: Main script for the Streamlit chatbot interface.
- **requirements.txt**: Lists all dependencies.
- **.env**: Contains environment variables like LANGCHAIN_API_KEY (not included in the repository for security).

---

## 📈 Future Improvements
- Expanding model options to support additional LLMs.
- Adding context retention for more conversational interactions.
- Integrating with additional APIs for extended capabilities.

