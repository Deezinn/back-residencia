from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ErrorModel(BaseModel):
   userId: str
   documentClassification: str
   image: str
   created_at: Optional[datetime]
