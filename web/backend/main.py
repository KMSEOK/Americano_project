from app.models import init_db
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"hello": "world"}

# if __name__ == "__main__":
#     init_db()
#     uvicorn.run("main:app", host="docker_app", port=8080, reload=True)
