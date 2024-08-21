from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from my_api.initialize_api import router
app=FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow any origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


app.include_router(router)