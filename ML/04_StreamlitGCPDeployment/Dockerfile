# Use a slim Python image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt, model and application code
COPY requirements.txt .
COPY bigmart_model.pkl . 
COPY app.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Streamlit defaults to port 8501, and Cloud Run expects applications to listen on the port specified by the PORT environment variable.
# We need to tell Streamlit to listen on the Cloud Run provided PORT.
# Also, Streamlit needs to be told not to open a browser.
ENV PORT 8080
EXPOSE $PORT

# Command to run your Streamlit application
CMD ["streamlit", "run", "app.py", "--server.port", "8080", "--server.address", "0.0.0.0"]