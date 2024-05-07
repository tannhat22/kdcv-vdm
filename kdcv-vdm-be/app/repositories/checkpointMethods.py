from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException

from app import schemas, models

class CheckpointMethodRepository:
    def create_checkpointMethod(self, db: Session, checkpointMethod: schemas.CheckpointMethodBase):
        newCheckpointMethod = models.CheckpointMethod(**checkpointMethod.model_dump())
        db.add(newCheckpointMethod)
        db.commit()
        db.refresh(newCheckpointMethod)
        return newCheckpointMethod

    def get_checkpointMethod(self, db: Session, id: int):
        checkpointMethod = db.query(models.CheckpointMethod).filter(models.CheckpointMethod.id == id).first()
        if not checkpointMethod:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"CheckpointMethod with the id: `{id}` not found")
        return checkpointMethod

    def get_checkpointMethods(self, db: Session):
        return db.query(models.CheckpointMethod).all()
    
    def get_checkpointMethods_of_jobCategory(self, db: Session, job_category_id: int):
        checkpointMethods = db.query(models.CheckpointMethod).filter(models.CheckpointMethod.job_category_id == job_category_id).all()
        if not checkpointMethods:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"CheckpointMethods with the job_category_id: `{job_category_id}` not found")
        return checkpointMethods

    def update_checkpointMethod(self, db: Session, id: int, checkpointMethodUpdate: schemas.CheckpointMethodBase):
        checkpointMethod = db.query(models.CheckpointMethod).filter(models.CheckpointMethod.id == id)
        if not checkpointMethod.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"CheckpointMethod with the id: `{id}` not found")
        checkpointMethod.update(checkpointMethodUpdate.model_dump())
        db.commit()
        return {"message": "CheckpointMethod updated successfully"}

    def delete_checkpointMethod(self, db: Session, id: int):
        checkpointMethod = db.query(models.CheckpointMethod).filter(models.CheckpointMethod.id == id)
        if not checkpointMethod.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"CheckpointMethod with the id: `{id}` not found")
        checkpointMethod.delete()
        db.commit()
        return {"message": "CheckpointMethod deleted successfully"}
    
    def delete_checkpointMethods_of_jobCategory(self, db: Session, job_category_id: int):
        checkpointMethods = db.query(models.CheckpointMethod).filter(models.CheckpointMethod.job_category_id == job_category_id)
        if not checkpointMethods.all():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"CheckpointMethods with the job_category_id: `{job_category_id}` not found")
        checkpointMethods.delete()
        db.commit()
        return {"message": "All checkpointMethods of jobCategory deleted successfully"}
    
    def check_job_category_id_exist(self, db: Session, job_category_id: int):
        return db.query(models.JobCategory).filter(models.JobCategory.id == job_category_id).first()
