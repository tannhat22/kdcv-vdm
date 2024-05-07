from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException

from app import schemas, models

class MachineRepository:
    def create_machine(self, db: Session, machine: schemas.MachineBase):
        newMachine = models.Machine(**machine.model_dump())
        db.add(newMachine)
        db.commit()
        db.refresh(newMachine)
        return newMachine

    def get_machine(self, db: Session, serial_no: str):
        machine = db.query(models.Machine).filter(models.Machine.serial_no == serial_no).first()
        if not machine:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Machine with the serial_no: `{serial_no}` not found")
        return machine

    def get_machines(self, db: Session):
        return db.query(models.Machine).all()
    
    def get_machines_with_job_id(self, db: Session, job_id: str):
        machine = db.query(models.Machine).filter(models.Machine.job_id == job_id).all()
        return machine

    def update_machine(self, db: Session, serial_no: str, machineUpdate: schemas.MachineBase):
        machine = db.query(models.Machine).filter(models.Machine.serial_no == serial_no) 
        if not machine.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Machine with the serial_no: `{serial_no}` not found")
        machine.update(machineUpdate.model_dump())
        db.commit()
        return {"message": "Machine updated successfully"}

    def delete_machine(self, db: Session, serial_no: str):
        machine = db.query(models.Machine).filter(models.Machine.serial_no == serial_no)
        if not machine.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Machine with the serial_no: `{serial_no}` not found")
        machine.delete()
        db.commit()
        return {"message": "Machine deleted successfully"}
    
    def check_serial_no_exist(self, db: Session, serial_no: str):
        return db.query(models.Machine).filter(models.Machine.serial_no == serial_no).first()
    
    def check_job_id_exist(self, db: Session, job_id: str):
        return db.query(models.Job).filter(models.Job.job_id == job_id).first()