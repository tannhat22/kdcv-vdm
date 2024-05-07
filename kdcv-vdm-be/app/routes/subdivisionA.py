from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas, database
from app.authenticator import user_dep
from app.repositories import RecordRepository, SubdivisionARepository

def admin_dep(user: schemas.User = Depends(user_dep)):
    if not user.is_admin:
        raise HTTPException(403,"User does not have permission to access this content")

# router = APIRouter(tags=["SubdivisionA"], dependencies=[Depends(admin_dep)])
router = APIRouter(tags=["SubdivisionA"])

get_db = database.get_db
RecordRepo = RecordRepository()
SubdivisionARepo = SubdivisionARepository()

# Tạo 1 subdivisionA mới
@router.post("", status_code=status.HTTP_201_CREATED, response_model=schemas.SubdivisionABase)
def create_subdivisionA(request: schemas.SubdivisionABase, db: Session = Depends(get_db)):
    if not RecordRepo.check_record_id_exist(db,request.record_id):
        raise HTTPException(status_code=400, detail=f"Record_id: `{request.record_id}` is non-exists")
    return SubdivisionARepo.create_subdivisionA(db, request)

# Lấy toàn bộ dữ liệu subdivisionAs bao gồm cả ID
@router.get("", response_model=List[schemas.SubdivisionAId])
def get_subdivisionAs(db: Session = Depends(get_db)):
    return SubdivisionARepo.get_subdivisionAs(db)

# Lấy toàn bộ dữ liệu subdivisionAs của một record_id không kèm ID
# @router.get("/record/{record_id}", status_code=status.HTTP_200_OK, response_model=List[schemas.SubdivisionABase])
# def get_subdivisionAs_of_record(record_id: str, db: Session = Depends(get_db)):
#     return SubdivisionARepo.get_subdivisionAs_of_record(db, record_id)

# Lấy toàn bộ dữ liệu subdivisionAs của một record_id kèm ID
@router.get("/record/{record_id}", status_code=status.HTTP_200_OK, response_model=List[schemas.SubdivisionAId])
def get_subdivisionAs_of_recordId(record_id: str, db: Session = Depends(get_db)):
    return SubdivisionARepo.get_subdivisionAs_of_recordId(db, record_id)

# Lấy dữ liệu của một subdivisionA theo ID
@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.SubdivisionABase)
def get_subdivisionA(id: int, db: Session = Depends(get_db)):
    return SubdivisionARepo.get_subdivisionA(db, id)

# Sửa dữ liệu subdivisionA
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_subdivisionA(id: int, request: schemas.SubdivisionABase, db: Session = Depends(get_db)):
    if not RecordRepo.check_record_id_exist(db,request.record_id):
        raise HTTPException(status_code=400, detail=f"Record_id: `{request.record_id}` is non-exists")
    return SubdivisionARepo.update_subdivisionA(db, id, request)

# Xóa toàn bộ dữ liệu subdivisionAs của một record_id
@router.delete('/record/{record_id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy_subdivisionAs_of_record(record_id: str, db: Session = Depends(get_db)):
    return SubdivisionARepo.delete_subdivisionAs_of_recordId(db, record_id)

# Xóa dữ liệu một subdivisionA theo ID
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return SubdivisionARepo.delete_subdivisionA(db, id)
