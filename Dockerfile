FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ /app/

ENV PORT=8080

RUN ls -la /app && ls -la /app/model

CMD gunicorn --bind 0.0.0.0:$PORT app:app