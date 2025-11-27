# 🚀 Automatic Blog Writer
An intelligent **Streamlit + Flask + LangChain + OpenAI** application that generates high-quality, structured blog posts from any topic.

## ✨ Features

-  Generate full blog posts (introduction → body → conclusion)  
-  Uses **OpenAI GPT-4o Mini** through LangChain  
-  Clean and fast **Streamlit UI**  
-  Flask backend API  

## 🧠 Tech Stack

### **Frontend**
- Streamlit  
- Python Requests  

### **Backend**
- Flask (REST API)

### **AI Engine**
- LangChain  
- OpenAI GPT-4o Mini models  

### **Environment & Tools**
- Conda  
- Python 3.10  
- dotenv  

## ⚙️ Setup Guide

1️⃣ Clone the Repository
- git clone https://github.com/linara03/Automatic-Blog-Writer.git
- cd automatic-blog-writer

2️⃣ Create a Conda Environment
- conda create -n agentapp python=3.10
- conda activate agentapp

3️⃣ Install Dependencies
- pip install -r requirements.txt

4️⃣ Add Your OpenAI API Key
- Create a .env file in the project root:
- OPENAI_API_KEY=your_api_key_here

5️⃣ Start the Backend
- python endpoint.py

6️⃣ Start the Frontend
- Open a second terminal:
 - conda activate agentapp
 - streamlit run app.py
