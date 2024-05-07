from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException

from app import schemas, models

class SubdivisionCRepository:
    def create_subdivisionC(self, db: Session, subdivisionC: schemas.SubdivisionCBase):
        newSubdivisionC = models.SubdivisionC(**subdivisionC.model_dump())
        db.add(newSubdivisionC)
        db.commit()
        db.refresh(newSubdivisionC)
        return newSubdivisionC

    def get_subdivisionC(self, db: Session, id: int):
        subdivisionC = db.query(models.SubdivisionC).filter(models.SubdivisionC.id == id).first()
        if not subdivisionC:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"SubdivisionC with the id: `{id}` not found")
        return subdivisionC

    def get_subdivisionCs(self, db: Session):
        return db.query(models.SubdivisionC).all()

    def get_subdivisionCs_of_recordId(self, db: Session, record_id: str):
        subdivisionCs = db.query(models.SubdivisionC).filter(models.SubdivisionC.record_id == record_id).all()
        if not subdivisionCs:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"SubdivisionCs with the record_id: `{record_id}` not found")
        return subdivisionCs

    def update_subdivisionC(self, db: Session, id: int, subdivisionCUpdate: schemas.SubdivisionCBase):
        subdivisionC = db.query(models.SubdivisionC).filter(models.SubdivisionC.id == id)
        if not subdivisionC.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"SubdivisionC with the id: `{id}` not found")
        subdivisionC.update(subdivisionCUpdate.model_dump())
        db.commit()
        return {"message": "SubdivisionC updated successfully"}

    def delete_subdivisionC(self, db: Session, id: int):
        subdivisionC = db.query(models.SubdivisionC).filter(models.SubdivisionC.id == id)
        if not subdivisionC.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"SubdivisionC with the id: `{id}` not found")
        subdivisionC.delete()
        db.commit()
        return {"message": "SubdivisionC deleted successfully"}

    def delete_subdivisionCs_of_recordId(self, db: Session, record_id: str):
        subdivisionCs = db.query(models.SubdivisionC).filter(models.SubdivisionC.record_id == record_id)
        if not subdivisionCs.all():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"SubdivisionCs with the record_id: `{record_id}` not found")
        subdivisionCs.delete()
        db.commit()
        return {"message": "SubdivisionCs deleted successfully"}
