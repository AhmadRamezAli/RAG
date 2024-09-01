from fastapi import FastAPI,Body, File, Form, UploadFile,Request
from fastapi import APIRouter
from core.get_answer_from_model import get_answer_from_model
from core.llm_factory.llm_initializer import LLM_initializer
from pydantic import BaseModel
from typing import List
import os
router = APIRouter(prefix="/api")


class QueryRequest(BaseModel):
    chunks: int
    numofresults: int
    question: str
    filenames: List[str]
    modelname:str

@router.post("/query/")
async def postq(query_request: QueryRequest):
    chunks = query_request.chunks
    numofresults = query_request.numofresults
    question = query_request.question
    filepaths = [f"core/data/{file}" for file in query_request.filenames]
    initializer = LLM_initializer()
    client= initializer.create(query_request.modelname)
    # Ensure the client creator is not None
    if client is None:
        raise ValueError(f"Failed to create a client for model: {query_request.modelname}")
    
    client=client.create()
    result = get_answer_from_model(client,filepaths, chunks, numofresults, question)
    print(result)
    return result