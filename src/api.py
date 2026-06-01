from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "project": "Personal Finance & Investment Intelligence Platform",
        "status": "running"
    }
