from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas, database
from app.authenticator import user_dep
from app.repositories import JobRepository

def admin_dep(user: schemas.User = Depends(user_dep)):
    if not user.is_admin:
        raise HTTPException(403,"User does not have permission to access this content")

# router = APIRouter(tags=["Jobs"], dependencies=[Depends(admin_dep)])
router = APIRouter(tags=["Jobs"])

get_db = database.get_db
JobRepo = JobRepository()

# Tạo 1 job mới
@router.post("", status_code=status.HTTP_201_CREATED)
def create_job(request: schemas.JobBase, db: Session = Depends(get_db)):
    if JobRepo.check_job_id_exist(db, request.job_id):
        raise HTTPException(status_code=400, detail="Job_ID is already exists")
    return JobRepo.create_job(db, request)

# Lấy toàn bộ dữ liệu jobs
@router.get("", response_model=List[schemas.Job])
def get_jobs(db: Session = Depends(get_db)):
    return JobRepo.get_jobs(db)

# Lấy dữ liệu 1 job theo job_id
@router.get("/{job_id}", status_code=status.HTTP_200_OK, response_model=schemas.Job)
def get_job(job_id: str, db: Session = Depends(get_db)):
    return JobRepo.get_job(db, job_id)

# Sửa dữ liệu job
@router.put("/{job_id}", status_code=status.HTTP_202_ACCEPTED)
def update_job(job_id: str, request: schemas.JobBase, db: Session = Depends(get_db)):
    # Kiểm tra có bị trùng job_id với Job khác sau khi sửa không
    if job_id != request.job_id:
        if JobRepo.check_job_id_exist(db, request.job_id):
            raise HTTPException(status_code=400, detail="New Job_ID is already exists")
    return JobRepo.update_job(db, id, request)

# Xóa dữ liệu job
@router.delete('/{job_id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(job_id: str, db: Session = Depends(get_db)):
    return JobRepo.delete_job(db, job_id)