from fastapi import APIRouter, status, Depends, HTTPException, Response
from ..schemas import UserOut, UserCreate, User
from ..models import session_local, Users, get_db
from sqlalchemy.orm import Session

router = APIRouter()

# def get_users(db: Session = Depends(get_db)):
@router.get("/", status_code=status.HTTP_200_OK, response_model=list[UserOut])
def get_users(db: Session = Depends(get_db)):
    users = db.query(Users).all()
    return users

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(Users).filter(Users.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id: {id} does not exists.")
    return user

@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = Users(**user.dict())
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
        raise HTTPException(status_code=status.HTTP_404_PAGE_NOT_FOUND,
        detail=f"user with id: {id} does not exists.")

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
        raise HTTPException(status_code=status.HTTP_404_PAGE_NOT_FOUND,
        detail=f"user with id: {id} does not exists.")

    user_query.update(updated_user.dict(), synchronize_session=False)
    db.commit()

    return user_query.first()
 
