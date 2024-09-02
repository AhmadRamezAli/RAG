from fastapi import FastAPI,Body, File, Form, UploadFile,Request
from fastapi import APIRouter
from core.get_answer_from_model import get_answer_from_model
from core.llm_factory.llm_initializer import LLM_initializer
from pydantic import BaseModel
from typing import List
import os
router = APIRouter(prefix="/api")


@router.post("/uploadfile/")
async def postupload(
    files:list [UploadFile]=File(...)
):
    print(len(files))
    for file in files:
        print(f"Received file: {file.filename}, size: {file.size} bytes")
        file_location = f"core/data/{file.filename}"
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


