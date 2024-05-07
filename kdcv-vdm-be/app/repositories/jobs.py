from datetime import datetime
import time
from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException

from app import schemas, models

class JobRepository:
    def create_job(self, db: Session, job: schemas.JobBase):
        unix_timestamp_now = datetime.now().timestamp()
        newJob = models.Job(**job.model_dump(), drafted_date=unix_timestamp_now, updated_date=0.0)
        db.add(newJob)
        db.commit()
        db.refresh(newJob)
        return newJob

    def get_job(self, db: Session, job_id: str):
        job = db.query(models.Job).filter(models.Job.job_id == job_id).first()
        if not job:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Job with the job_id: `{job_id}` not found")
        return job

    def get_jobs(self, db: Session):
        return db.query(models.Job).all()

    def update_job(self, db: Session, job_id: str, jobUpdate: schemas.JobBase):
        job = db.query(models.Job).filter(models.Job.job_id == job_id)
        if not job.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Job with the job_id: `{job_id}` not found")
        job.update(jobUpdate.model_dump())
        db.commit()
        return {"message": "Job updated successfully"}

    def delete_job(self, db: Session, job_id: str):
        job = db.query(models.Job).filter(models.Job.job_id == job_id)
        if not job.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Job with the job_id: `{job_id}` not found")
        job.delete()
        db.commit()
        return {"message": "Job deleted successfully"}
    
    def check_job_id_exist(self, db: Session, job_id: str):
        return db.query(models.Job).filter(models.Job.job_id == job_id).first()
