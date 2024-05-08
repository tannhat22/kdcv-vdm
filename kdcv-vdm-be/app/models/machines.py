from sqlalchemy import Boolean, BigInteger, Column, ForeignKey, Float, Integer, String, Time
from sqlalchemy.orm import relationship

from app.database import Base

class Job(Base):
    __tablename__ = "jobs"

    job_id = Column(String(255), primary_key=True)
    job_name = Column(String(255))
    drafted_place = Column(String(255))
    drafter = Column(String(255))
    # confirm = Column(String(255))
    # recognize = Column(String(255))
    drafted_date = Column(BigInteger)
    updated_date = Column(BigInteger)

    machines = relationship('Machine', back_populates='job')
    jobCategories = relationship('JobCategory', back_populates='job')


class JobCategory(Base):
    __tablename__ = "job_categories"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(String(255), ForeignKey('jobs.job_id'))
    step = Column(Integer)
    checkpoint_category = Column(String(255))
    checkpoint_method = Column(String(255))
    checkpoint_position = Column(String(255))
    confirmation_explanation = Column(String(255))
    device_change = Column(Boolean)
    part_code_change = Column(Boolean)
    power_outage = Column(Boolean)
    is_measure = Column(Boolean)
    is_auto = Column(Boolean)
    A_sub = Column(Boolean)
    B_sub = Column(Boolean)
    C_sub = Column(Boolean)

    job = relationship('Job', back_populates='jobCategories')
    # checkpoint_method = relationship('CheckpointMethod', back_populates='job_category')


# class CheckpointMethod(Base):
#     __tablename__ = "checkpoint_methods"

#     id = Column(Integer, primary_key=True, index=True)
#     desc = Column(String(255))
#     position = Column(String(255))
#     confirmation_explanation = Column(String(255))
#     job_category_id = Column(Integer, ForeignKey('job_categories.id'))

#     job_category = relationship('JobCategory', back_populates='checkpoint_method')


class Machine(Base):
    __tablename__ = "machines"
    
    serial_no = Column(String(255), primary_key=True)
    species = Column(String(255))
    name = Column(String(255))
    job_id = Column(String(255), ForeignKey('jobs.job_id'))

    job = relationship('Job', back_populates='machines')
