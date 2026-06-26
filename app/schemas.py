from datetime import datetime 
from typing import Optional 
from pydantic import BaseModel 

class ModelCreate(BaseModel): 
    name: str 
    description: Optional[str]=None 
    owner: Optional[str]=None 

class ModelRead(BaseModel):
    id:int 
    name:str 
    description: Optional[str]=None 
    owner: Optional[str]=None 
    created_at: datetime 
    model_config = {"from_attributes":True} #lets pydantic reads from sqlalchemy object

class VersionCreate(BaseModel):
    framework: Optional[str]=None
    metrics: Optional[dict]=None 
    artifact_url: Optional[str]=None
    created_by: Optional[str]=None

class VersionRead(BaseModel):
    id: int 
    model_id: int 
    version_number: int
    framework: Optional[str]=None
    metrics: Optional[dict]=None 
    artifact_url: Optional[str]=None
    stage: str
    created_by: Optional[str]=None
    created_at: datetime
    model_config = {"from_attributes":True}