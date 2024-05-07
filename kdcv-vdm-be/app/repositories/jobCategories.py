from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException

from app import schemas, models

class JobCategoryRepository:
    def create_jobCategory(self, db: Session, jobCategory: schemas.JobCategoryBase):
        newJobCategory = models.JobCategory(**jobCategory.model_dump())
        db.add(newJobCategory)
        db.commit()
        db.refresh(newJobCategory)
        return newJobCategory

    def get_jobCategory(self, db: Session, id: int):
        jobCategory = db.query(models.JobCategory).filter(models.JobCategory.id == id).first()
        if not jobCategory:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"JobCategory with the id: `{id}` not found")
        return jobCategory

    def get_jobCategories(self, db: Session):
        return db.query(models.JobCategory).all()
    
    def get_jobCategories_of_job(self, db: Session, job_id: str):
        jobCategories = db.query(models.JobCategory).filter(models.JobCategory.job_id == job_id).all()
        if not jobCategories:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"JobCategories with the job_id: `{job_id}` not found")
        return jobCategories

    def update_jobCategory(self, db: Session, id: int, jobCategoryUpdate: schemas.JobCategoryBase):
        jobCategory = db.query(models.JobCategory).filter(models.JobCategory.id == id)
        if not jobCategory.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"JobCategory with the id: `{id}` not found")
        jobCategory.update(jobCategoryUpdate.model_dump())
        db.commit()
        return {"message": "JobCategory updated successfully"}

    def delete_jobCategory(self, db: Session, id: int):
        jobCategory = db.query(models.JobCategory).filter(models.JobCategory.id == id)
        if not jobCategory.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"JobCategory with the id: `{id}` not found")
        jobCategory.delete()
        db.commit()
        return {"message": "JobCategory deleted successfully"}
    
    def delete_jobCategories_of_job(self, db: Session, job_id: str):
        jobCategories = db.query(models.JobCategory).filter(models.JobCategory.job_id == job_id)
        if not jobCategories.all():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"JobCategories with the job_id: `{job_id}` not found")
        jobCategories.delete()
        db.commit()
        return {"message": "All jobCategories of job deleted successfully"}
    
    def check_job_id_exist(self, db: Session, job_id: str):
        return db.query(models.Job).filter(models.Job.job_id == job_id).first()