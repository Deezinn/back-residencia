from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ErrorModel(BaseModel):
   userId: str
   codigo: int
   guid: str
   documentClassification: str
   image: str
   # resultado: str
   created_at: datetime = Field(default_factory=datetime.utcnow)
