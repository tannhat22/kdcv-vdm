from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException

from app import schemas, models

class RecordRepository:
    def create_record(self, db: Session, record: schemas.RecordBase):
        newRecord = models.Record(**record.model_dump())
        db.add(newRecord)
        db.commit()
        db.refresh(newRecord)
        return newRecord

    def get_record(self, db: Session, record_id: str):
        record = db.query(models.Record).filter(models.Record.record_id == record_id).first()
        if not record:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Record with the record_id: `{record_id}` not found")
        return record

    def get_records(self, db: Session):
        return db.query(models.Record).all()

    def update_record(self, db: Session, record_id: str, recordUpdate: schemas.RecordBase):
        record = db.query(models.Record).filter(models.Record.record_id == record_id)
        if not record.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Record with the record_id: `{record_id}` not found")
        record.update(recordUpdate.model_dump())
        db.commit()
        return {"message": "Record updated successfully"}

    def delete_record(self, db: Session, record_id: str):
        record = db.query(models.Record).filter(models.Record.record_id == record_id)
        if not record.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Record with the record_id: `{record_id}` not found")
        record.delete()
        db.commit()
        return {"message": "Record deleted successfully"}
    
    def check_record_id_exist(self, db: Session, record_id: str):
        return db.query(models.Record).filter(models.Record.record_id == record_id).first()
