FROM python:3.9-slim-bullseye

WORKDIR /app

COPY ./requirements.txt .
RUN pip install --requirement requirements.txt

COPY ./app.py .

RUN mkdir -p /data

CMD ["python", "./app.py"]
