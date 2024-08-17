import chromadb
chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(name="data-from-file")
