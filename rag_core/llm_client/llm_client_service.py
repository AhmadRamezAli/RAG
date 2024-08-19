from abc import ABC, abstractmethod

# Define the interface
class LLMClientService(ABC):
    @abstractmethod
    def chat(self,role,content) -> str:
        """send quesiton to llm and return the response"""
        pass

