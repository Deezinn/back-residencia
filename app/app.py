
from fastapi.middleware.cors import CORSMiddleware
from main import app

origins = [
   "http://localhost:3001",
   "http://localhost:3000",
   "http://localhost",
]

app.middleware(
   CORSMiddleware,
   allow_origins=origins,
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"],
)