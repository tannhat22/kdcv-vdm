from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas, database
from app.authenticator import user_dep
from app.repositories import RecordRepository, SubdivisionCRepository

def admin_dep(user: schemas.User = Depends(user_dep)):
    if not user.is_admin:
        raise HTTPException(403,"User does not have permission to access this content")

# router = APIRouter(tags=["SubdivisionC"], dependencies=[Depends(admin_dep)])
router = APIRouter(tags=["SubdivisionC"])

get_db = database.get_db
RecordRepo = RecordRepository()
SubdivisionCRepo = SubdivisionCRepository()

# Tạo 1 subdivisionC mới
@router.post("", status_code=status.HTTP_201_CREATED, response_model=schemas.SubdivisionCBase)
def create_subdivisionC(request: schemas.SubdivisionCBase, db: Session = Depends(get_db)):
    if not RecordRepo.check_record_id_exist(db,request.record_id):
        raise HTTPException(status_code=400, detail=f"Record_id: `{request.record_id}` is non-exists")
    return SubdivisionCRepo.create_subdivisionC(db, request)

# Lấy toàn bộ dữ liệu subdivisionCs bao gồm cả ID
@router.get("", response_model=List[schemas.SubdivisionCId])
def get_subdivisionCs(db: Session = Depends(get_db)):
    return SubdivisionCRepo.get_subdivisionCs(db)

# Lấy toàn bộ dữ liệu subdivisionCs của một record_id không kèm ID
# @router.get("/record/{record_id}", status_code=status.HTTP_200_OK, response_model=List[schemas.SubdivisionCBase])
# def get_subdivisionCs_of_record(record_id: str, db: Session = Depends(get_db)):
#     return SubdivisionCRepo.get_subdivisionCs_of_record(db, record_id)

# Lấy toàn bộ dữ liệu subdivisionCs của một record_id kèm ID
@router.get("/record/{record_id}", status_code=status.HTTP_200_OK, response_model=List[schemas.SubdivisionCId])
def get_subdivisionCs_of_recordId(record_id: str, db: Session = Depends(get_db)):
    return SubdivisionCRepo.get_subdivisionCs_of_recordId(db, record_id)

# Lấy dữ liệu của một subdivisionC theo ID
@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.SubdivisionCBase)
def get_subdivisionC(id: int, db: Session = Depends(get_db)):
    return SubdivisionCRepo.get_subdivisionC(db, id)

# Sửa dữ liệu subdivisionC
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_subdivisionC(id: int, request: schemas.SubdivisionCBase, db: Session = Depends(get_db)):
    if not RecordRepo.check_record_id_exist(db,request.record_id):
        raise HTTPException(status_code=400, detail=f"Record_id: `{request.record_id}` is non-exists")
    return SubdivisionCRepo.update_subdivisionC(db, id, request)

# Xóa toàn bộ dữ liệu subdivisionCs của một record_id
@router.delete('/record/{record_id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy_subdivisionCs_of_record(record_id: str, db: Session = Depends(get_db)):
    return SubdivisionCRepo.delete_subdivisionCs_of_recordId(db, record_id)

# Xóa dữ liệu một subdivisionC theo ID
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return SubdivisionCRepo.delete_subdivisionC(db, id)
