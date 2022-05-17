import uuid
from pydantic import BaseModel, UUID4
from .models import GradeType
from typing import Optional


class User(BaseModel):
    id: int
    name: str
    grade: GradeType
    introduction: str

    class Config:
        orm_mode = True

class UserOut(BaseModel):
    id: int
    name: str
    grade: GradeType
    introduction: str

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    # id: UUID4 = uuid.uuid4()
    name: str
    grade: GradeType
    introduction: str

    class Config:
        orm_mode = True


