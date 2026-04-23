# LLM Groq Chatbot

## 🚀 Setup Instructions

1. Clone repo:
   git clone https://github.com/yourname/LLM-Groq-Chatbot.git

2. Go to folder:
   cd LLM-Groq-Chatbot

3. Create virtual environment:
   python -m venv groq_env
   .\groq_env\Scripts\activate

4. Install dependencies:
   pip install -r requirements.txt

5. Add API key:
   Create .env file and add:
   GROQ_API_KEY=your_api_key

6. Run backend:
   uvicorn backend.main:app --reload

7. Run frontend:
   cd frontend
   streamlit run app.py
