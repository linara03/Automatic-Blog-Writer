# Automatic-Blog-Writer 🚀

A Streamlit + Flask + LangChain + OpenAI–powered AI application that generates high-quality blog posts based on any user-provided topic.

📌 Overview
Built with:
Frontend: Streamlit
Backend: Flask 
AI Engine: LangChain + OpenAI GPT-4o models
Environment: Conda
Users enter a blog topic → the backend sends it to the AI model → a fully structured blog post is returned and displayed.

⚙️Setup Guide
1️⃣ Clone the Repository
git clone https://github.com/your-username/automatic-blog-writer.git
cd automatic-blog-writer

2️⃣ Create Conda Environment
conda create -n agentapp python=3.10
conda activate agentapp

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Add Your OpenAI API Key
Create a .env file in the project root:
OPENAI_API_KEY=your_key

5️⃣ Start Backend (Flask API)
python endpoint.py

6️⃣ Start Frontend (Streamlit)
streamlit run app.py

Link: https://linara03-automatic-blog-writer-app-sfcc9e.streamlit.app/
