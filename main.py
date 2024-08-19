from fastapi import FastAPI
from my_api.initialize_api import router
app=FastAPI()

app.include_router(router)