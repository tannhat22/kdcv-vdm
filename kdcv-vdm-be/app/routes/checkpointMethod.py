from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas, database
from app.authenticator import user_dep
from app.repositories import CheckpointMethodRepository

def admin_dep(user: schemas.User = Depends(user_dep)):
    if not user.is_admin:
        raise HTTPException(403,"User does not have permission to access this content")

# router = APIRouter(tags=["CheckpointMethods"], dependencies=[Depends(admin_dep)])
router = APIRouter(tags=["CheckpointMethods"])

get_db = database.get_db
CheckpointMethodRepo = CheckpointMethodRepository()

# Tạo 1 checkpointMethod mới
@router.post("", status_code=status.HTTP_201_CREATED, response_model=schemas.CheckpointMethodBase)
def create_checkpointMethod(request: schemas.CheckpointMethodBase, db: Session = Depends(get_db)):
    if not CheckpointMethodRepo.check_job_category_id_exist(db, request.job_category_id):
        raise HTTPException(status_code=400, detail=f"JobCategory_ID: `{request.job_category_id}` is non-exists")
    return CheckpointMethodRepo.create_checkpointMethod(db, request)

# Lấy toàn bộ dữ liệu checkpointMethods bao gồm cả ID
@router.get("", response_model=List[schemas.CheckpointMethodId])
def get_checkpointMethods(db: Session = Depends(get_db)):
    return CheckpointMethodRepo.get_checkpointMethods(db)

# Lấy toàn bộ dữ liệu checkpointMethods của một job_category_id không kèm ID
# @router.get("/job/{job_category_id}", status_code=status.HTTP_200_OK, response_model=List[schemas.CheckpointMethodBase])
# def get_checkpointMethods_of_job(job_category_id: str, db: Session = Depends(get_db)):
#     return CheckpointMethodRepo.get_checkpointMethods_of_job(db, job_category_id)

# Lấy toàn bộ dữ liệu checkpointMethods của một job_category_id kèm ID
@router.get("/jobCategory/{job_category_id}", status_code=status.HTTP_200_OK, response_model=List[schemas.CheckpointMethodId])
def get_checkpointMethods_of_jobCategory(job_category_id: int, db: Session = Depends(get_db)):
    return CheckpointMethodRepo.get_checkpointMethods_of_jobCategory(db, job_category_id)

# Lấy dữ liệu của một checkpointMethod theo ID
@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.CheckpointMethodBase)
def get_checkpointMethod(id: int, db: Session = Depends(get_db)):
    return CheckpointMethodRepo.get_checkpointMethod(db, id)

# Sửa dữ liệu checkpointMethod
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_checkpointMethod(id: int, request: schemas.CheckpointMethodBase, db: Session = Depends(get_db)):
    if not CheckpointMethodRepo.check_job_category_id_exist(db, request.job_category_id):
        raise HTTPException(status_code=400, detail=f"JobCategory_ID: `{request.job_category_id}` is non-exists")
    return CheckpointMethodRepo.update_checkpointMethod(db, id, request)

# Xóa toàn bộ dữ liệu checkpointMethods của một job_category_id
@router.delete('/jobCategory/{job_category_id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy_checkpointMethods_of_jobCategory(job_category_id: int, db: Session = Depends(get_db)):
    return CheckpointMethodRepo.delete_checkpointMethods_of_jobCategory(db, job_category_id)

# Xóa dữ liệu một checkpointMethod theo ID
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return CheckpointMethodRepo.delete_checkpointMethod(db, id)
