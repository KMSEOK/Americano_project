from app.models import init_db
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app.routers import user, job

app = FastAPI()

origins = ["http://localhost:3030", "localhost:3030", "http://localhost:3000", "localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router, prefix="/api/v1/users")
app.include_router(job.router, prefix="/api/v1/jobs")


if __name__ == "__main__":
    init_db()
    uvicorn.run("main:app", host="app", port=8080, reload=True)
