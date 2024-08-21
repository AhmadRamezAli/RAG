from fastapi import FastAPI,Body, File, Form, UploadFile,Request
from fastapi import APIRouter
from rag_core.get_answer_from_model import get_answer_from_model
from pydantic import BaseModel
from typing import List
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
    files:list [UploadFile]=File(...)
):
    print(len(files))
    for file in files:
        print(f"Received file: {file.filename}, size: {file.size} bytes")
        file_location = f"rag_core/src/{file.filename}"

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
async def postq(
    request: Request
):
    data = await request.json()
    print(data)
    chunks = data.get('chunks')
    numofresults = data.get('numofresults')
    question = data.get('question')
    filepaths = data.get('filepaths')

    print("WAWWWWWWWWWWWWWWWWW")
    new_filepaths = [f"rag_core/src/{filepath}" for filepath in filepaths]
    print(new_filepaths)

    result = get_answer_from_model( new_filepaths ,chunks, numofresults, question)
    return result    
    
 