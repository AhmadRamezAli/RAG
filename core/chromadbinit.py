import chromadb
chroma_client = chromadb.PersistentClient(path="./chromadb/")
collection = chroma_client.get_or_create_collection(name="data-from-file")
