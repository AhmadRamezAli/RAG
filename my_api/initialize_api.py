from fastapi import FastAPI,Body
from fastapi import APIRouter
from rag_core.get_answer_from_model import get_answer_from_model

router = APIRouter(prefix="/api")

@router.get("/")
def root():
    return {"message": "Hello tt"}


@router.post("/query/")
def postq(payload: dict = Body(...)):
    return get_answer_from_model(r"rag_core/src/aram_mohammed.pdf",payload['chunks'],payload['numofresults'],payload['question'])
