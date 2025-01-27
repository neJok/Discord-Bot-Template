ARG PYTHON_VERSION=3.12.0
FROM python:${PYTHON_VERSION}-slim as base

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD python bot.py
