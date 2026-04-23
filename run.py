import subprocess

# Start FastAPI backend
backend = subprocess.Popen(
    ["python", "-m", "uvicorn", "backend.main:app", "--reload"]
)

# Start Streamlit frontend
frontend = subprocess.Popen(
    ["python", "-m", "streamlit", "run", "frontend/app.py"]
)

# Wait for both
backend.wait()
frontend.wait()