from pydantic import BaseModel
from .models import GradeType, StatusType, PlaceType


class User(BaseModel):
    id: int
    name: str
    grade: GradeType
    introduction: str
    hashed_password: str

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
    # grade: GradeType
    introduction: str
    hashed_password: str

    class Config:
        orm_mode = True


class JobOut(BaseModel):
    id: int
    user_id: int
    title: str
    description: str
    place: PlaceType
    reawrd_money: int
    reward_item: str
    status: StatusType
    time_required: int

    class Config:
        orm_mode = True


class JobCreate(BaseModel):
    user_id: int
    title: str
    description: str
    place: PlaceType
    reawrd_money: int
    reward_item: str
    status: StatusType
    time_required: int

    class Config:
        orm_mode = True
