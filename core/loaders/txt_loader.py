from langchain_community.document_loaders import TextLoader
from loaders.document_loader import DocumentLoader
class TxtLoader(DocumentLoader):
    def __init__(self, file_path: str):
        self.file_path = file_path
    
    def load(self) -> str:
        loader = TextLoader(self.file_path)
        documents = loader.load()
        return documents[0].page_content