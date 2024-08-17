from loaders.documen_loader import DocumentLoader


class Convertor:
    def __init__(self,loader:DocumentLoader):
        self.loader=loader
    def convert(self) -> str:
       return self.loader.load()