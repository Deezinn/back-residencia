from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.service.image_service import send_image_to_api

router = APIRouter()

@router.post('/upload')
async def upload_image(image: UploadFile = File(...),documentClassification: str = Form(...)):
   try:
      response = await send_image_to_api(image,documentClassification)
      return {"message": "Imagem enviada com sucesso!", "response": response}
   except Exception as e:
      raise HTTPException(status_code=500, detail=str(e))
