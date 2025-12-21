FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
COPY jobchg_pipeline_model.pkl . 
COPY app.py .

RUN pip install --no-cache-dir -r requirements.txt

# Streamlit specific settings for Cloud Run
ENV PORT 8080

# Command to run Streamlit
CMD uvicorn app:app --host 0.0.0.0 --port ${PORT:-8080}