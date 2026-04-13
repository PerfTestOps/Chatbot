# Use Python base image
FROM python:3.10-slim

WORKDIR /app

# Copy requirements and install
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy all files
COPY . .

# Expose Streamlit default port
EXPOSE 8501

# Run Streamlit chatbot
CMD ["streamlit", "run", "chatbot.py", "--server.port=8501", "--server.address=0.0.0.0"]
