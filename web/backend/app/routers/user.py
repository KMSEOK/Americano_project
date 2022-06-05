from fastapi import APIRouter, status, Depends, HTTPException
from ..schemes import UserOut, UserCreate, User
from ..models import Users, get_db
from sqlalchemy.orm import Session

# auth.
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Optional, Union
from passlib.context import CryptContext

router = APIRouter()

# >>>> start auth settings.
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    """このTokenDataの型って何に使われるんだろう?"""
    name: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    True if password matched the hash, else False.
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def authenticate_user(db: Session = Depends(get_db)) -> bool:
    """if does not exists user or failed to authenticate password, return False"""
    return False


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# @router.post("/token")
# def token(form_data: OAuth2PasswordRequestForm = Depends()):
    
#  <<<< end auth settings.

# def get_users(db: Session = Depends(get_db)):
@router.get("/", status_code=status.HTTP_200_OK, response_model=list[UserOut])
def get_users(db: Session = Depends(get_db)):
    users = db.query(Users).all()
    return users


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(Users).filter(Users.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id: {id} does not exists.",
        )
    return user


# ここでHash化してパスワードを保存する。
@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """새로운 사용자를 만든다."""
    user_data = user.dict()
    user_data["hashed_password"] = get_password_hash(user_data["hashed_password"])
    new_user = Users(**user_data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.delete("/delete/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    """사용자를 삭제한다.
    TODO: 자기만의 계자를 삭제할 수 있도록 하고, 다른 사람의 계정을 삭제하지 않도록 함.
    """
    user_query = db.query(Users).filter(Users.id == id)
    user = user_query.first()

    if user == None:
        raise HTTPException(
            status_code=status.HTTP_404_PAGE_NOT_FOUND,
            detail=f"user with id: {id} does not exists.",
        )

    user_query.delete(synchronize_session=False)
    db.commit()


@router.put("/update/{id}")
def update_user(id: int, updated_user: User, db: Session = Depends(get_db)):
    """사용자를 개신한다.
    TODO: 자기만의 계자를 개신할 수 있도록 하고, 다른 사람의 계정을 개신하지 않도록 함.
    """
    user_query = db.query(Users).filter(Users.id == id)
    user = user_query.first()

    if user == None:
        raise HTTPException(
            status_code=status.HTTP_404_PAGE_NOT_FOUND,
            detail=f"user with id: {id} does not exists.",
        )

    user_query.update(updated_user.dict(), synchronize_session=False)
    db.commit()

    return user_query.first()
