from langchain.text_splitter import CharacterTextSplitter
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from ollama import Client
from Convertor import Convertor
from langchain.text_splitter import CharacterTextSplitter
from Spliter import split_text_into_chunks
from PDFLoader import PDFLoader 
from ChromaDB import collection
import uuid

documents=PDFLoader("aram mohammed.pdf")
documents= Convertor(documents)
docs=documents.convert()

docs = split_text_into_chunks(docs,500,10)

# Generate unique IDs for each document
ids = [str(uuid.uuid4()) for _ in range(len(docs))]


collection.add(
    documents=docs ,
    ids=ids
)
results = collection.query(
    query_texts=["what is MVC"], # Chroma will embed this for you
    n_results=2 # how many results to return
)
print(results)





# client = Client(host='http://172.25.1.139:11434')
# response = client.chat(model='llama3', messages=[
#   {
#     'role': 'user',
#     'content': 'هل تعرف العربية',
#   },
# ])
# print(response)



# x= (embeddings.get_query_embedding("ho"))

