from fastapi import APIRouter, HTTPException
from bson import ObjectId
from app.service.error_service import get_error_by_id

router = APIRouter()

@router.get("/documents/{id}")
async def get_document(id: str):
   error = await get_error_by_id(id)
   if not error:
      raise HTTPException(status_code=404, detail="Documento não encontrado")
   error["id"] = str(error["_id"])
   del error["_id"]
   return error
