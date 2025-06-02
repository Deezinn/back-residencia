from bson import ObjectId
from app.db.mongo import db
import os

collection_name = os.getenv('MONGO_COLLECTION')
collection = db[collection_name]

async def get_error_by_id(id: str):
   if not ObjectId.is_valid(id):
      return None
   error = await collection.find_one({"_id": ObjectId(id)})
   return error
