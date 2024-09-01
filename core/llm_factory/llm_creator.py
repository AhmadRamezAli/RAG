
from abc import ABC, abstractmethod
from core.llm_client.llm_client_service import LLMClientService

class LLMClientCreator(ABC):
    @abstractmethod
    def create(self) -> LLMClientService:
        """send quesiton to llm and return the response"""
        pass

