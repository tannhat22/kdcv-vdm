from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas, database
from app.authenticator import user_dep
from app.repositories import RecordRepository

def admin_dep(user: schemas.User = Depends(user_dep)):
    if not user.is_admin:
        raise HTTPException(403,"User does not have permission to access this content")

# router = APIRouter(tags=["Records"], dependencies=[Depends(admin_dep)])
router = APIRouter(tags=["Records"])

get_db = database.get_db
RecordRepo = RecordRepository()

# Tạo 1 record mới
@router.post("", status_code=status.HTTP_201_CREATED)
def create_record(request: schemas.RecordBase, db: Session = Depends(get_db)):
    if RecordRepo.check_record_id_exist(db, request.record_id):
        raise HTTPException(status_code=400, detail="Record_ID is already exists")
    return RecordRepo.create_record(db, request)

# Lấy toàn bộ dữ liệu records
@router.get("", response_model=List[schemas.Record])
def get_records(db: Session = Depends(get_db)):
    return RecordRepo.get_records(db)

# Lấy dữ liệu 1 record theo record_id
@router.get("/{record_id}", status_code=status.HTTP_200_OK, response_model=schemas.Record)
def get_record(record_id: str, db: Session = Depends(get_db)):
    return RecordRepo.get_record(db, record_id)

# Sửa dữ liệu record
@router.put("/{record_id}", status_code=status.HTTP_202_ACCEPTED)
def update_record(record_id: str, request: schemas.RecordBase, db: Session = Depends(get_db)):
    # Kiểm tra có bị trùng record_id với Record khác sau khi sửa không
    if record_id != request.record_id:
        if RecordRepo.check_record_id_exist(db, request.record_id):
            raise HTTPException(status_code=400, detail="New Record_ID is already exists")
    return RecordRepo.update_record(db, id, request)

# Xóa dữ liệu record
@router.delete('/{record_id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(record_id: str, db: Session = Depends(get_db)):
    return RecordRepo.delete_record(db, record_id)