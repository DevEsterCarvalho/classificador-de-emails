FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install torch==2.8.0
RUN pip install transformers==4.30.0 flask==3.1.2 requests gunicorn

COPY src/ ./src

ENV FLASK_APP=src/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

EXPOSE 5000

CMD ["flask", "run"]
