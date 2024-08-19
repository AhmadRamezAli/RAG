from abc import ABC, abstractmethod
from rag_core.llm_client.llm_client_service import LLMClientService
from ollama import Client
from dotenv import load_dotenv
import os


load_dotenv()

hiast_server = os.getenv('HIAST_OLLAMA_URL')
hiast_model = os.getenv('HIAST_OLLAMA_MODEL')
# Define the interface
class HiastClient(LLMClientService):
    
    def __init__(self):
        self.client = Client(hiast_server)
    def chat(self,role,content) -> str:
        response = self.client.chat(model=hiast_model, messages=[
        {
            'role': role,
            'content': content,
        },
        ])
        return response

