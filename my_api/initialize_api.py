from fastapi import FastAPI,Body, File, Form, UploadFile,Request
from fastapi import APIRouter
from rag_core.get_answer_from_model import get_answer_from_model
from pydantic import BaseModel
from typing import List
import os
router = APIRouter(prefix="/api")

class QueryRequest(BaseModel):
    chunks: int
    numofresults: int
    question: str
    filenames: List[str]
@router.get("/")
def root():
    return {"message": "Hello tt"}

@router.post("/uploadfile/")
async def postupload(
    files:list [UploadFile]=File(...)
):
    print(len(files))
    for file in files:
        print(f"Received file: {file.filename}, size: {file.size} bytes")
        file_location = f"rag_core/src/{file.filename}"
        if os.path.exists(file_location):
            print(f"File {file.filename} already exists at {file_location}. Skipping save.")
            continue 
        try:
            # Save the file
            with open(file_location, "wb") as f:
                f.write(await file.read())
            
            print(f"File saved to: {file_location}")

        
        except Exception as e:
            print(f"Error occurred: {e}")
            return {"message": "Error processing file", "error": str(e)}
    return  {"message": "file saved saccussefully"}



@router.post("/query/")
async def postq(query_request: QueryRequest):
    chunks = query_request.chunks
    numofresults = query_request.numofresults
    question = query_request.question
    filepaths = [f"rag_core/src/{file}" for file in query_request.filenames]

    result = get_answer_from_model(filepaths, chunks, numofresults, question)
    print(result)
    return result