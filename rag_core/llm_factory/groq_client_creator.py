from abc import ABC, abstractmethod
from rag_core.llm_client.groq_client import GroqClient
from rag_core.llm_factory.llm_creator import LLMClientCreator
from rag_core.llm_client.llm_client_service import LLMClientService
from groq import Groq
from dotenv import load_dotenv
from dotenv import dotenv_values
import os


load_dotenv()
mysecrets = dotenv_values(".secret")
groq_model = os.getenv('QROQ_MODEL')

# Define the interface
class GroqClientCreator(LLMClientCreator):
    
    def create(self) ->LLMClientCreator :
        return GroqClient()
 


