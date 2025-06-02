from fastapi import FastAPI
from app.controller.image_controller import router as image_router
from app.controller.error_controller import router as error_router


app = FastAPI()

app.include_router(error_router, prefix="/api", tags=["Documents"])
app.include_router(image_router, prefix="/images", tags=["Images"])

@app.get("/")
def read_root():
   return {"Hello": "World"}
