# Use Python as base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy model and scripts
COPY model /app/model
COPY scripts/score.py /app/score.py
COPY requirements.txt /app/requirements.txt 

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose API port
EXPOSE 8000

# Run FastAPI app
CMD ["uvicorn", "score:app", "--host", "0.0.0.0", "--port", "8000"]
