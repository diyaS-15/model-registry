from datetime import datetime
from sqlalchemy import func 
from sqlalchemy.orm import relationship 
from app.database import Base 

from sqlalchemy import (
    Column, 
    Integer, 
    String, 
    ForeignKey, 
    DateTime, 
    JSON,
)

class Model(Base):
    __tablename__ = "models"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True, nullable=False)
    description = Column(String, nullable=True)
    owner = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    versions = relationship(
        "ModelVersions",
        back_populates="model",
        cascade="all, delete-orphan",
    )

class ModelVersion(Base):
    __tablename__= "versions"
    id = Column(Integer, primary_key=True, index=True)
    model_id=Column(Integer, ForeignKey("models.id"), nullable=False, index=True)
    version_number = Column(Integer, nullable=False)
    framework = Column(String, nullable=True)
    metrics = Column(JSON, nullable=True)
    artifact_uri = Column(String, nullable=True)
    stage = Column(String, nullable=False, default="archived")
    created_by = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)

model = relationship("Model", back_populates="versions")


