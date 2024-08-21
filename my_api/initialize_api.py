from fastapi import FastAPI,Body, File, Form, UploadFile
from fastapi import APIRouter
from rag_core.get_answer_from_model import get_answer_from_model
from pydantic import BaseModel
from typing import Optional
router = APIRouter(prefix="/api")


class RequestModel(BaseModel):
    chunks: int
    numofresults: int
    question: str
    file:UploadFile
@router.get("/")
def root():
    return {"message": "Hello tt"}

@router.post("/uploadfile/")
async def postupload(
    file: UploadFile
):
    print(f"Received file: {file.filename}, size: {file.size} bytes")
    file_location = f"rag_core/src/{file.filename}"

    try:
        # Save the file
        with open(file_location, "wb") as f:
            f.write(await file.read())
        
        print(f"File saved to: {file_location}")
        return  {"message": "file saved saccussefully"}
    
    except Exception as e:
        print(f"Error occurred: {e}")
        return {"message": "Error processing file", "error": str(e)}
    


@router.post("/query/")
async def postq(
    chunks: int = Form(...),
    numofresults: int = Form(...),
    question: str = Form(...),
    filepath: str = Form(...),
):
    file_locat= "rag_core/src/"+filepath
    print(file_locat)
    result = get_answer_from_model(file_locat, chunks, numofresults, question)
        
    return  result
 