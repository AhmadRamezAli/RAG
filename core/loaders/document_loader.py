from abc import ABC, abstractmethod

# Define the interface
class DocumentLoader(ABC):
    @abstractmethod
    def load(self) -> str:
        """Load the document content and return it as a string."""
        pass
