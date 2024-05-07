from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas, database
from app.authenticator import user_dep
from app.repositories import RecordRepository, SubdivisionSpecialRepository

def admin_dep(user: schemas.User = Depends(user_dep)):
    if not user.is_admin:
        raise HTTPException(403,"User does not have permission to access this content")

# router = APIRouter(tags=["SubdivisionSpecial"], dependencies=[Depends(admin_dep)])
router = APIRouter(tags=["SubdivisionSpecial"])

get_db = database.get_db
RecordRepo = RecordRepository()
SubdivisionSpecialRepo = SubdivisionSpecialRepository()

# Tạo 1 subdivisionSpecial mới
@router.post("", status_code=status.HTTP_201_CREATED, response_model=schemas.SubdivisionSpecialBase)
def create_subdivisionSpecial(request: schemas.SubdivisionSpecialBase, db: Session = Depends(get_db)):
    if not RecordRepo.check_record_id_exist(db,request.record_id):
        raise HTTPException(status_code=400, detail=f"Record_id: `{request.record_id}` is non-exists")
    return SubdivisionSpecialRepo.create_subdivisionSpecial(db, request)

# Lấy toàn bộ dữ liệu subdivisionSpecials bao gồm cả ID
@router.get("", response_model=List[schemas.SubdivisionSpecialId])
def get_subdivisionSpecials(db: Session = Depends(get_db)):
    return SubdivisionSpecialRepo.get_subdivisionSpecials(db)

# Lấy toàn bộ dữ liệu subdivisionSpecials của một record_id không kèm ID
# @router.get("/record/{record_id}", status_code=status.HTTP_200_OK, response_model=List[schemas.SubdivisionSpecialBase])
# def get_subdivisionSpecials_of_record(record_id: str, db: Session = Depends(get_db)):
#     return SubdivisionSpecialRepo.get_subdivisionSpecials_of_record(db, record_id)

# Lấy toàn bộ dữ liệu subdivisionSpecials của một record_id kèm ID
@router.get("/record/{record_id}", status_code=status.HTTP_200_OK, response_model=List[schemas.SubdivisionSpecialId])
def get_subdivisionSpecials_of_recordId(record_id: str, db: Session = Depends(get_db)):
    return SubdivisionSpecialRepo.get_subdivisionSpecials_of_recordId(db, record_id)

# Lấy dữ liệu của một subdivisionSpecial theo ID
@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.SubdivisionSpecialBase)
def get_subdivisionSpecial(id: int, db: Session = Depends(get_db)):
    return SubdivisionSpecialRepo.get_subdivisionSpecial(db, id)

# Sửa dữ liệu subdivisionSpecial
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_subdivisionSpecial(id: int, request: schemas.SubdivisionSpecialBase, db: Session = Depends(get_db)):
    if not RecordRepo.check_record_id_exist(db,request.record_id):
        raise HTTPException(status_code=400, detail=f"Record_id: `{request.record_id}` is non-exists")
    return SubdivisionSpecialRepo.update_subdivisionSpecial(db, id, request)

# Xóa toàn bộ dữ liệu subdivisionSpecials của một record_id
@router.delete('/record/{record_id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy_subdivisionSpecials_of_record(record_id: str, db: Session = Depends(get_db)):
    return SubdivisionSpecialRepo.delete_subdivisionSpecials_of_recordId(db, record_id)

# Xóa dữ liệu một subdivisionSpecial theo ID
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return SubdivisionSpecialRepo.delete_subdivisionSpecial(db, id)
