from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.upload_api import router as upload_router
from api.query_api import router as query_router
import uvicorn
import os



app=FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow any origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


app.include_router(upload_router)
app.include_router(query_router)