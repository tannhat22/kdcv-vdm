from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException

from app import schemas, models

class SubdivisionSpecialRepository:
    def create_subdivisionSpecial(self, db: Session, subdivisionSpecial: schemas.SubdivisionSpecialBase):
        newSubdivisionSpecial = models.SubdivisionSpecial(**subdivisionSpecial.model_dump())
        db.add(newSubdivisionSpecial)
        db.commit()
        db.refresh(newSubdivisionSpecial)
        return newSubdivisionSpecial

    def get_subdivisionSpecial(self, db: Session, id: int):
        subdivisionSpecial = db.query(models.SubdivisionSpecial).filter(models.SubdivisionSpecial.id == id).first()
        if not subdivisionSpecial:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"SubdivisionSpecial with the id: `{id}` not found")
        return subdivisionSpecial

    def get_subdivisionSpecials(self, db: Session):
        return db.query(models.SubdivisionSpecial).all()

    def get_subdivisionSpecials_of_recordId(self, db: Session, record_id: str):
        subdivisionSpecials = db.query(models.SubdivisionSpecial).filter(models.SubdivisionSpecial.record_id == record_id).all()
        if not subdivisionSpecials:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"SubdivisionSpecials with the record_id: `{record_id}` not found")
        return subdivisionSpecials

    def update_subdivisionSpecial(self, db: Session, id: int, subdivisionSpecialUpdate: schemas.SubdivisionSpecialBase):
        subdivisionSpecial = db.query(models.SubdivisionSpecial).filter(models.SubdivisionSpecial.id == id)
        if not subdivisionSpecial.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"SubdivisionSpecial with the id: `{id}` not found")
        subdivisionSpecial.update(subdivisionSpecialUpdate.model_dump())
        db.commit()
        return {"message": "SubdivisionSpecial updated successfully"}

    def delete_subdivisionSpecial(self, db: Session, id: int):
        subdivisionSpecial = db.query(models.SubdivisionSpecial).filter(models.SubdivisionSpecial.id == id)
        if not subdivisionSpecial.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"SubdivisionSpecial with the id: `{id}` not found")
        subdivisionSpecial.delete()
        db.commit()
        return {"message": "SubdivisionSpecial deleted successfully"}

    def delete_subdivisionSpecials_of_recordId(self, db: Session, record_id: str):
        subdivisionSpecials = db.query(models.SubdivisionSpecial).filter(models.SubdivisionSpecial.record_id == record_id)
        if not subdivisionSpecials.all():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"SubdivisionSpecials with the record_id: `{record_id}` not found")
        subdivisionSpecials.delete()
        db.commit()
        return {"message": "SubdivisionSpecials deleted successfully"}
