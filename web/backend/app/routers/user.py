from fastapi import APIRouter, status, Depends
from ..schemas import UserOut
from ..models import session_local, Users
from sqlalchemy.orm import Session

router = APIRouter()

# def get_users(db: Session = Depends(get_db)):
@router.get("/get_users", status_code=status.HTTP_200_OK)
def get_users():
    # res = db.query(Users).all()
    # print(res)
    return {"msg": "successfully get users."}

