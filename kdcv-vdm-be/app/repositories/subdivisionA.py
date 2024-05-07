from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException

from app import schemas, models

class SubdivisionARepository:
    def create_subdivisionA(self, db: Session, subdivisionA: schemas.SubdivisionABase):
        newSubdivisionA = models.SubdivisionA(**subdivisionA.model_dump())
        db.add(newSubdivisionA)
        db.commit()
        db.refresh(newSubdivisionA)
        return newSubdivisionA

    def get_subdivisionA(self, db: Session, id: int):
        subdivisionA = db.query(models.SubdivisionA).filter(models.SubdivisionA.id == id).first()
        if not subdivisionA:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"SubdivisionA with the id: `{id}` not found")
        return subdivisionA

    def get_subdivisionAs(self, db: Session):
        return db.query(models.SubdivisionA).all()

    def get_subdivisionAs_of_recordId(self, db: Session, record_id: str):
        subdivisionAs = db.query(models.SubdivisionA).filter(models.SubdivisionA.record_id == record_id).all()
        if not subdivisionAs:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"SubdivisionAs with the record_id: `{record_id}` not found")
        return subdivisionAs

    def update_subdivisionA(self, db: Session, id: int, subdivisionAUpdate: schemas.SubdivisionABase):
        subdivisionA = db.query(models.SubdivisionA).filter(models.SubdivisionA.id == id)
        if not subdivisionA.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"SubdivisionA with the id: `{id}` not found")
        subdivisionA.update(subdivisionAUpdate.model_dump())
        db.commit()
        return {"message": "SubdivisionA updated successfully"}

    def delete_subdivisionA(self, db: Session, id: int):
        subdivisionA = db.query(models.SubdivisionA).filter(models.SubdivisionA.id == id)
        if not subdivisionA.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"SubdivisionA with the id: `{id}` not found")
        subdivisionA.delete()
        db.commit()
        return {"message": "SubdivisionA deleted successfully"}

    def delete_subdivisionAs_of_recordId(self, db: Session, record_id: str):
        subdivisionAs = db.query(models.SubdivisionA).filter(models.SubdivisionA.record_id == record_id)
        if not subdivisionAs.all():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"SubdivisionAs with the record_id: `{record_id}` not found")
        subdivisionAs.delete()
        db.commit()
        return {"message": "SubdivisionAs deleted successfully"}
