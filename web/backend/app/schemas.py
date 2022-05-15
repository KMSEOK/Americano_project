from pydantic import BaseModel
from .models import GradeType

class UserOut(BaseModel):
    id: int
    name: str
    grade: GradeType
    introduction: str
