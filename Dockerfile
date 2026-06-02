FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python3", "-m", "uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]
