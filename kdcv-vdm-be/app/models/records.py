from sqlalchemy import Column, ForeignKey, Integer, BigInteger, Float, String
from sqlalchemy.orm import relationship

from app.database import Base

class Record(Base):
    __tablename__ = "records"

    record_id = Column(String(255), primary_key=True)
    unix_millis_created_time = Column(BigInteger)
    shift = Column(String(255))
    job_id = Column(String(255))
    machine_serial = Column(String(255))
    checker = Column(String(255))
    confirmer = Column(String(255))

    subdivision_A = relationship('SubdivisionA', back_populates='record')
    subdivision_B = relationship('SubdivisionB', back_populates='record')
    subdivision_C = relationship('SubdivisionC', back_populates='record')
    subdivision_special = relationship('SubdivisionSpecial', back_populates='record')

class SubdivisionA(Base):
    __tablename__ = "A_subdivisions"

    id = Column(Integer, primary_key=True, index=True)
    record_id = Column(String(255), ForeignKey('records.record_id'))
    mpa = Column(Float)
    kgf_per_cm2 = Column(Float)
    result = Column(String(255))

    record = relationship('Record', back_populates='subdivision_A')

class SubdivisionB(Base):
    __tablename__ = "B_subdivisions"

    id = Column(Integer, primary_key=True, index=True)
    record_id = Column(String(255), ForeignKey('records.record_id'))
    mpa = Column(Float)
    kgf_per_cm2 = Column(Float)
    result = Column(String(255))

    record = relationship('Record', back_populates='subdivision_B')

class SubdivisionC(Base):
    __tablename__ = "C_subdivisions"

    id = Column(Integer, primary_key=True, index=True)
    record_id = Column(String(255), ForeignKey('records.record_id'))
    mpa = Column(Float)
    kgf_per_cm2 = Column(Float)
    result = Column(String(255))

    record = relationship('Record', back_populates='subdivision_C')

class SubdivisionSpecial(Base):
    __tablename__ = "special_subdivisions"

    id = Column(Integer, primary_key=True, index=True)
    record_id = Column(String(255), ForeignKey('records.record_id'))
    time = Column(Integer)
    reason = Column(String(255))
    result_bf = Column(String(255))
    result_af = Column(String(255))
    result = Column(String(255))

    record = relationship('Record', back_populates='subdivision_special')