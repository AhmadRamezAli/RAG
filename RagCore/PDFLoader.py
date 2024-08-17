from langchain_community.document_loaders import PyPDFLoader

from DocumentLoader import DocumentLoader
class PDFLoader(DocumentLoader):
    def __init__(self, file_path: str):
        self.file_path = file_path
    
    def load(self) -> str:
        loader = PyPDFLoader(self.file_path)
        documents = loader.load()
        return "\n".join([doc.page_content for doc in documents])
