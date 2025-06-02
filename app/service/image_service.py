import base64
import requests
from fastapi import UploadFile
from dotenv import load_dotenv
import os

from app.models.error_model import ErrorModel
from app.repository.error_repository import save_error

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
API_URL = os.getenv("API_URL")
userId = os.getenv('USER_ID')

async def send_image_to_api(image: UploadFile, documentClassification: str):
   content = await image.read()
   encoded_image = base64.b64encode(content).decode('utf-8')

   payload = {
      "image": encoded_image,
      "userId": userId,
      "documentClassification": documentClassification
   }

   headers = {
      "Authorization": API_TOKEN,
   }


   response = requests.post(API_URL, json=payload, headers=headers)
   response.raise_for_status()
   api_response = response.json()

   codigo = response.status_code

   try:
      resultado = api_response["resultados"][0]
      guid = api_response["guid"]
   except (KeyError, IndexError):
      raise ValueError("Resposta da API não tem os campos esperados")

   error = ErrorModel(
      userId=userId,
      codigo=codigo,
      guid=guid,
      documentClassification=documentClassification,
      image=encoded_image,
      # resultado=resultado
   )
   await save_error(error)

   return api_response
