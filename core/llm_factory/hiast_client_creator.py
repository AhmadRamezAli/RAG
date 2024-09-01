from abc import ABC, abstractmethod
from core.llm_client.hiast_client import HiastClient
from core.llm_factory.llm_creator import LLMClientCreator
from core.llm_client.llm_client_service import LLMClientService
from groq import Groq
from dotenv import load_dotenv
from dotenv import dotenv_values
import os


load_dotenv()
mysecrets = dotenv_values(".secret")
groq_model = os.getenv('QROQ_MODEL')

# Define the interface
class HiastClientCreator(LLMClientCreator):
    
    def create(self) ->HiastClient :
        return HiastClient()
 


