from fastapi import APIRouter, status, Depends, HTTPException
from ..schemas import JobOut, JobCreate
from ..models import Jobs, get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/", status_code=status.HTTP_200_OK, response_model=list[JobOut])
def get_jobs(db: Session = Depends(get_db)):
    jobs = db.query(Jobs).all()
    return jobs

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=JobOut)
def get_job(id: int, db: Session = Depends(get_db)):
    job = db.query(Jobs).filter(Jobs.id == id).first()
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f"job with id: {id} does not exists.")
    return job

@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    new_job = Jobs(**job.dict())
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job

@router.delete("/delete/{id}")
def delete_job(id: int, db: Session = Depends(get_db)):
    """아르바이트를 삭제한다.
        TODO: 자기만의 아르바이트를 삭제할 수 있도록 하고, 다른 사람의 아르바이트을 삭제하지 않도록 함.
    """
    job_query = db.query(Jobs).filter(Jobs.id == id)
    job = job_query.first()

    if job == None:
        raise HTTPException(status_code=status.HTTP_404_PAGE_NOT_FOUND,
        detail=f"job with id: {id} does not exists.")

    job_query.delete(synchronize_session=False)
    db.commit()


@router.put("/update/{id}")
def update_job(id: int, updated_job: JobOut, db: Session = Depends(get_db)):
    """사용자를 개신한다.
        TODO: 자기만의 계자를 개신할 수 있도록 하고, 다른 사람의 계정을 개신하지 않도록 함.
    """
    job_query = db.query(Jobs).filter(Jobs.id == id)
    job = job_query.first()

    if job == None:
        raise HTTPException(status_code=status.HTTP_404_PAGE_NOT_FOUND,
        detail=f"job with id: {id} does not exists.")

    job_query.update(updated_job.dict(), synchronize_session=False)
    db.commit()

    return job_query.first()
 
