from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas, database
from app.authenticator import user_dep
from app.repositories import JobCategoryRepository

def admin_dep(user: schemas.User = Depends(user_dep)):
    if not user.is_admin:
        raise HTTPException(403,"User does not have permission to access this content")

# router = APIRouter(tags=["JobCategories"], dependencies=[Depends(admin_dep)])
router = APIRouter(tags=["JobCategories"])

get_db = database.get_db
JobCategoryRepo = JobCategoryRepository()

# Tạo 1 jobCategory mới
@router.post("", status_code=status.HTTP_201_CREATED, response_model=schemas.JobCategoryBase)
def create_jobCategory(request: schemas.JobCategoryBase, db: Session = Depends(get_db)):
    if not JobCategoryRepo.check_job_id_exist(db, request.job_id):
        raise HTTPException(status_code=400, detail=f"Job_ID: `{request.job_id}` is non-exists")
    return JobCategoryRepo.create_jobCategory(db, request)

# Lấy toàn bộ dữ liệu jobCategories bao gồm cả ID
@router.get("", response_model=List[schemas.JobCategoryId])
def get_jobCategories(db: Session = Depends(get_db)):
    return JobCategoryRepo.get_jobCategories(db)

# Lấy toàn bộ dữ liệu jobCategories của một job_id không kèm ID
# @router.get("/job/{job_id}", status_code=status.HTTP_200_OK, response_model=List[schemas.JobCategoryBase])
# def get_jobCategories_of_job(job_id: str, db: Session = Depends(get_db)):
#     return JobCategoryRepo.get_jobCategories_of_job(db, job_id)

# Lấy toàn bộ dữ liệu jobCategories của một job_id kèm ID
@router.get("/job/{job_id}", status_code=status.HTTP_200_OK, response_model=List[schemas.JobCategoryId])
def get_jobCategories_of_jobId(job_id: str, db: Session = Depends(get_db)):
    return JobCategoryRepo.get_jobCategories_of_job(db, job_id)

# Lấy dữ liệu của một jobCategory theo ID
@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.JobCategoryBase)
def get_jobCategory(id: int, db: Session = Depends(get_db)):
    return JobCategoryRepo.get_jobCategory(db, id)

# Sửa dữ liệu jobCategory
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_jobCategory(id: int, request: schemas.JobCategoryBase, db: Session = Depends(get_db)):
    if not JobCategoryRepo.check_job_id_exist(db, request.job_id):
        raise HTTPException(status_code=400, detail=f"Job_ID: `{request.job_id}` is non-exists")
    return JobCategoryRepo.update_jobCategory(db, id, request)

# Xóa toàn bộ dữ liệu jobCategories của một job_id
@router.delete('/job/{job_id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy_jobCategories_of_job(job_id: str, db: Session = Depends(get_db)):
    return JobCategoryRepo.delete_jobCategories_of_job(db, job_id)

# Xóa dữ liệu một jobCategory theo ID
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return JobCategoryRepo.delete_jobCategory(db, id)
