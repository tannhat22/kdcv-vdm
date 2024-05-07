from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas, database
from app.authenticator import user_dep
from app.repositories import RecordRepository, SubdivisionBRepository

def admin_dep(user: schemas.User = Depends(user_dep)):
    if not user.is_admin:
        raise HTTPException(403,"User does not have permission to access this content")

# router = APIRouter(tags=["SubdivisionB"], dependencies=[Depends(admin_dep)])
router = APIRouter(tags=["SubdivisionB"])

get_db = database.get_db
RecordRepo = RecordRepository()
SubdivisionBRepo = SubdivisionBRepository()

# Tạo 1 subdivisionB mới
@router.post("", status_code=status.HTTP_201_CREATED, response_model=schemas.SubdivisionBBase)
def create_subdivisionB(request: schemas.SubdivisionBBase, db: Session = Depends(get_db)):
    if not RecordRepo.check_record_id_exist(db,request.record_id):
        raise HTTPException(status_code=400, detail=f"Record_id: `{request.record_id}` is non-exists")
    return SubdivisionBRepo.create_subdivisionB(db, request)

# Lấy toàn bộ dữ liệu subdivisionBs bao gồm cả ID
@router.get("", response_model=List[schemas.SubdivisionBId])
def get_subdivisionBs(db: Session = Depends(get_db)):
    return SubdivisionBRepo.get_subdivisionBs(db)

# Lấy toàn bộ dữ liệu subdivisionBs của một record_id không kèm ID
# @router.get("/record/{record_id}", status_code=status.HTTP_200_OK, response_model=List[schemas.SubdivisionBBase])
# def get_subdivisionBs_of_record(record_id: str, db: Session = Depends(get_db)):
#     return SubdivisionBRepo.get_subdivisionBs_of_record(db, record_id)

# Lấy toàn bộ dữ liệu subdivisionBs của một record_id kèm ID
@router.get("/record/{record_id}", status_code=status.HTTP_200_OK, response_model=List[schemas.SubdivisionBId])
def get_subdivisionBs_of_recordId(record_id: str, db: Session = Depends(get_db)):
    return SubdivisionBRepo.get_subdivisionBs_of_recordId(db, record_id)

# Lấy dữ liệu của một subdivisionB theo ID
@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.SubdivisionBBase)
def get_subdivisionB(id: int, db: Session = Depends(get_db)):
    return SubdivisionBRepo.get_subdivisionB(db, id)

# Sửa dữ liệu subdivisionB
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_subdivisionB(id: int, request: schemas.SubdivisionBBase, db: Session = Depends(get_db)):
    if not RecordRepo.check_record_id_exist(db,request.record_id):
        raise HTTPException(status_code=400, detail=f"Record_id: `{request.record_id}` is non-exists")
    return SubdivisionBRepo.update_subdivisionB(db, id, request)

# Xóa toàn bộ dữ liệu subdivisionBs của một record_id
@router.delete('/record/{record_id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy_subdivisionBs_of_record(record_id: str, db: Session = Depends(get_db)):
    return SubdivisionBRepo.delete_subdivisionBs_of_recordId(db, record_id)

# Xóa dữ liệu một subdivisionB theo ID
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return SubdivisionBRepo.delete_subdivisionB(db, id)
