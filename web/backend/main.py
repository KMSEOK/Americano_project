from tkinter import Y
from app.models import init_db
from fastapi import FastAPI
import gunicorn

app = FastAPI()

@app.get("/")
def root():
    return {"hello": "world"}

if __name__ == "__main__":
    init_db()
    gunicorn.run("main:app", host="localhost", port=8080, reload=True)
