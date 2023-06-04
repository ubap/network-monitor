# syntax=docker/dockerfile:1

FROM python:3.12.0b1-bullseye

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

WORKDIR /app

COPY . .

CMD ["python3", "main.py"]
