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
from ollama import Client

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

question = "what is the outline of this paper"
results = collection.query(
    query_texts=[question], # Chroma will embed this for you
    n_results=10 # how many results to return
)

context=""
for doc in results["documents"][0]:
    context+=doc+"\n"



template=f"""
You are an assistant for question-answering tasks. 
Use the following pieces of retrieved context to answer the question. 
If you don't know the answer, just say that you don't know. 
Use five sentences minimum and keep the answer concise.
Question: {question} 
Context: {context} 
Answer:
"""



client = Client(host='http://172.25.1.141:11434')
response = client.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': template,
  },
])
print(response["message"]["content"])

