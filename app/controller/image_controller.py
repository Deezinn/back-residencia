from fastapi import APIRouter, UploadFile, File, HTTPException

router = APIRouter()

@router.post('/upload')
async def upload_image(file: UploadFile = file(...)):
   try:
      
      return {"Message": "Imagem enviada com sucesso!", "response": response}
   except Exception as e:
      raise HTTPException(status_code=500, detail=str(e))
