from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas, database
from app.authenticator import user_dep
from app.repositories import MachineRepository

def admin_dep(user: schemas.User = Depends(user_dep)):
    if not user.is_admin:
        raise HTTPException(403,"User does not have permission to access this content")

routerAdmin = APIRouter(tags=["Machines"], dependencies=[Depends(admin_dep)])
router = APIRouter(tags=["Machines"])
get_db = database.get_db
MachineRepo = MachineRepository()

# Tạo 1 machine mới
@router.post("", status_code=status.HTTP_201_CREATED)
def create_machine(request: schemas.MachineBase, db: Session = Depends(get_db)):
    if MachineRepo.check_serial_no_exist(db, request.serial_no):
        raise HTTPException(status_code=400, detail=f"Serial_no: `{request.serial_no}`  is already exists")
    if not MachineRepo.check_job_id_exist(db, request.job_id):
        raise HTTPException(status_code=400, detail=f"Job_ID: `{request.job_id}` is non-exists")
    return MachineRepo.create_machine(db, request)

# Lấy toàn bộ dữ liệu machines
@router.get("", response_model=List[schemas.MachineBase])
def get_machines(db: Session = Depends(get_db)):
    return MachineRepo.get_machines(db)

# Lấy dữ liệu 1 machine theo serial_no
@router.get("/{serial_no}", status_code=status.HTTP_200_OK, response_model=schemas.Machine)
def get_machine(serial_no: str, db: Session = Depends(get_db)):
    return MachineRepo.get_machine(db, serial_no)

# Sửa dữ liệu machine
@router.put("/{serial_no}", status_code=status.HTTP_202_ACCEPTED)
def update_machine(serial_no: str, request: schemas.MachineBase, db: Session = Depends(get_db)):
    if serial_no != request.serial_no:
        if MachineRepo.check_serial_no_exist(db, request.serial_no):
            raise HTTPException(status_code=400, detail="New serial_no is already exists")
    return MachineRepo.update_machine(db, serial_no, request)

# Xóa dữ liệu machine
@router.delete('/{serial_no}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(serial_no: str, db: Session = Depends(get_db)):
    return MachineRepo.delete_machine(db, serial_no)