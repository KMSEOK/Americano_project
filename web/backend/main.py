from app.models import init_db
from fastapi import FastAPI
import uvicorn
from app.routers import user

app = FastAPI()
app.include_router(user.router, prefix="/api/v1/users")

if __name__ == "__main__":
    init_db()
    uvicorn.run("main:app", host="app", port=8080, reload=True)
