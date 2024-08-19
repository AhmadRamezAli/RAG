from abc import ABC, abstractmethod
from rag_core.llm_client.llm_client_service import LLMClientService
from groq import Groq
from dotenv import load_dotenv
from dotenv import dotenv_values
import os


load_dotenv()
mysecrets = dotenv_values(".secret")
groq_model = os.getenv('QROQ_MODEL')

# Define the interface
class GroqClient(LLMClientService):
    
    def __init__(self):
        self.client = Groq(api_key = mysecrets["GROQ_API_KEY"])
    def chat(self,role,content) -> str:
        response = self.client.chat.completions.create(
        messages=[
            {
                "role": role,
                "content": content,
            }
        ],
        model=groq_model,
        )
       
        return response


