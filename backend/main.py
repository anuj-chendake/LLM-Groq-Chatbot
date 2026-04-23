from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from groq import Groq

# 🔹 Load environment variables
load_dotenv()

# 🔹 Initialize FastAPI
app = FastAPI()

# 🔹 Enable CORS (important for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 Load API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("❌ GROQ_API_KEY not found in .env file")

# 🔹 Initialize Groq client
client = Groq(api_key=api_key)

# 🔹 Request schema
class ChatRequest(BaseModel):
    message: str

# 🔹 Root endpoint
@app.get("/")
def home():
    return {"message": "✅ Backend is running successfully"}

# 🔹 Chat endpoint
@app.post("/chat")
def chat(request: ChatRequest):
    try:
        user_input = request.message

        # 🔥 Call Groq API (UPDATED MODEL)
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        # 🔹 Extract reply
        reply = response.choices[0].message.content

        return {
            "response": reply
        }

    except Exception as e:
        # 🔴 Return proper error for debugging
        return {
            "error": str(e)
        }
#.\groq_env\Scripts\Activate
#python -m uvicorn backend.main:app --reload
#python -m streamlit run frontend/app.py
#