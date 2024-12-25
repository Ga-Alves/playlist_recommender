FROM python:3.9-slim-bullseye

WORKDIR /app

COPY ./requirements.txt .
RUN pip install --requirement requirements.txt

COPY ./rulesGenerator.py .

CMD ["python", "./app.py"]
