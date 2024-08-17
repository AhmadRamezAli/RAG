from docx import Document
from DocumentLoader import DocumentLoader
class DocxLoader(DocumentLoader):
    def __init__(self, file_path: str):
        self.file_path = file_path
    
    def load(self) -> str:
        doc = Document(self.file_path)
        full_text = []
        for paragraph in doc.paragraphs:
            full_text.append(paragraph.text)
        return "\n".join(full_text)
