from app.models import init_db
from fastapi import FastAPI
import uvicorn
from app.routers import user, job

app = FastAPI()
app.include_router(user.router, prefix="/api/v1/users")
app.include_router(job.router, prefix="/api/v1/jobs")

if __name__ == "__main__":
    init_db()
    uvicorn.run("main:app", host="app", port=8080, reload=True)
