from app.db.mongo import db
from app.models.error_model import ErrorModel
import os

collection_name = os.getenv('MONGO_COLLECTION')
collection = db[collection_name]

async def save_error(error: ErrorModel):
   error_dict = error.dict()
   result = await collection.insert_one(error_dict)
   return str(result.inserted_id)


