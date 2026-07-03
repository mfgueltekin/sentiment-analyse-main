FROM python:3.11-slim

WORKDIR /app

# Requirements
COPY docs/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Code + Modelle
COPY src /app/src
COPY model /app/model

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
