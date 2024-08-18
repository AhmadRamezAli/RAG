from fastapi import FastAPI
from fastapi.params import Body
from postquerytest import postquery
app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello tt"}


@app.post("/query")
def postq(payload: dict = Body(...)):
    return postquery(r"src/aram_mohammed.pdf",payload['question']) 