import uuid
from rag_core.convertor import Convertor
from rag_core.spliter import split_text_into_chunks
from rag_core.loaders.pdf_loader import PDFLoader 
from rag_core.chromadbinit import collection
from rag_core.llm_client.hiast_client import HiastClient


def get_answer_from_model(docpath,chunks,numofresults,question):
    documents=PDFLoader(docpath)
    documents= Convertor(documents)
    docs=documents.convert()

    docs = split_text_into_chunks(docs,chunks,10)

    ids = [str(uuid.uuid4()) for _ in range(len(docs))]


    collection.add(
        documents=docs ,
        ids=ids
    )
    results = collection.query(
        query_texts=[question],
        n_results=numofresults # how many results to return
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



    client = HiastClient()
    response = client.chat('user',template)
    return response

