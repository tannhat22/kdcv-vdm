from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException

from app import schemas, models

class SubdivisionBRepository:
    def create_subdivisionB(self, db: Session, subdivisionB: schemas.SubdivisionBBase):
        newSubdivisionB = models.SubdivisionB(**subdivisionB.model_dump())
        db.add(newSubdivisionB)
        db.commit()
        db.refresh(newSubdivisionB)
        return newSubdivisionB

    def get_subdivisionB(self, db: Session, id: int):
        subdivisionB = db.query(models.SubdivisionB).filter(models.SubdivisionB.id == id).first()
        if not subdivisionB:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"SubdivisionB with the id: `{id}` not found")
        return subdivisionB

    def get_subdivisionBs(self, db: Session):
        return db.query(models.SubdivisionB).all()

    def get_subdivisionBs_of_recordId(self, db: Session, record_id: str):
        subdivisionBs = db.query(models.SubdivisionB).filter(models.SubdivisionB.record_id == record_id).all()
        if not subdivisionBs:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"SubdivisionBs with the record_id: `{record_id}` not found")
        return subdivisionBs

    def update_subdivisionB(self, db: Session, id: int, subdivisionBUpdate: schemas.SubdivisionBBase):
        subdivisionB = db.query(models.SubdivisionB).filter(models.SubdivisionB.id == id)
        if not subdivisionB.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"SubdivisionB with the id: `{id}` not found")
        subdivisionB.update(subdivisionBUpdate.model_dump())
        db.commit()
        return {"message": "SubdivisionB updated successfully"}

    def delete_subdivisionB(self, db: Session, id: int):
        subdivisionB = db.query(models.SubdivisionB).filter(models.SubdivisionB.id == id)
        if not subdivisionB.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"SubdivisionB with the id: `{id}` not found")
        subdivisionB.delete()
        db.commit()
        return {"message": "SubdivisionB deleted successfully"}

    def delete_subdivisionBs_of_recordId(self, db: Session, record_id: str):
        subdivisionBs = db.query(models.SubdivisionB).filter(models.SubdivisionB.record_id == record_id)
        if not subdivisionBs.all():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"SubdivisionBs with the record_id: `{record_id}` not found")
        subdivisionBs.delete()
        db.commit()
        return {"message": "SubdivisionBs deleted successfully"}
