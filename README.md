🚀 Automatic Blog Writer – AI-Powered Content Generator

An intelligent Streamlit + Flask + LangChain + OpenAI–based application that generates high-quality, structured blog posts from any topic.

📌 Features
✅ Generate full blog posts (intro → body → conclusion)
✅ Uses OpenAI GPT-4o Mini via LangChain
✅ Clean Streamlit UI
✅ Flask backend endpoint

🛠️ Tech Stack
Frontend
Streamlit

Backend
Flask (REST API)
Python Requests

AI / LLM
LangChain
OpenAI GPT-4o models

Environment & Tools
Conda
Python 3.10
dotenv

📁 Project Structure
Automatic-Blog-Writer/
│
├── app.py                  # Streamlit frontend
├── endpoint.py             # Flask backend API
│
├── backend/
│   ├── generate_blog.py    # Blog generation logic (LangChain + OpenAI)
│
├── requirements.txt        # Dependencies
├── .env                    # Environment variables (API Keys)
├── README.md               # Project documentation
└── ...

⚙️ Setup Guide

Follow these steps to run the project locally.

1️⃣ Clone the Repository
git clone https://github.com/your-username/automatic-blog-writer.git
cd automatic-blog-writer

2️⃣ Create a Conda Environment
conda create -n agentapp python=3.10
conda activate agentapp

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Add Your OpenAI API Key
Create a .env file in the project root:
OPENAI_API_KEY=your_api_key_here

5️⃣ Start the Backend (Flask API)
python endpoint.py

6️⃣ Start the Frontend (Streamlit App)
Open a second terminal:
conda activate agentapp
streamlit run app.py
