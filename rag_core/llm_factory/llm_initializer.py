

from rag_core.llm_factory.groq_client_creator import GroqClientCreator
from rag_core.llm_factory.hiast_client_creator import HiastClientCreator
from rag_core.llm_factory.llm_creator import LLMClientCreator
class LLM_initializer():
    
   def create(self,name:str) ->LLMClientCreator:
     if name=="groq(llama3-8b-8192)":
        return GroqClientCreator()
     if name=="llama3":
        return HiastClientCreator()
     
