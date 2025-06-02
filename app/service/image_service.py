import base64
import requests
from fastapi import UploadFile
from dotenv import load_dotenv
import os

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
   return response.json()
