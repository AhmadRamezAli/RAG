import uuid
from core.convertor import Convertor
from core.spliter import split_text_into_chunks
from core.loaders.pdf_loader import PDFLoader 
from core.chromadbinit import collection
from core.llm_client.hiast_client import HiastClient
from typing import List
from core.llm_client.groq_client import GroqClient
from core.llm_client.llm_client_service import LLMClientService
import json
from core.file_tracker import FileTracker
def get_answer_from_model(client:LLMClientService, docpaths :List[str] ,chunks,numofresults,question):
    
    ok= False
    
    if docpaths != FileTracker.static_file_path:
        FileTracker.static_file_path=docpaths
        fulldocs=[]
        for file in docpaths:
            
            docs=""
            documents=PDFLoader(file)
            documents= Convertor(documents)
            docs=documents.convert()
            docs = split_text_into_chunks(docs,chunks,10)
            fulldocs.extend(docs)

            ids = [str(uuid.uuid4()) for _ in range(len(fulldocs))]

        
            collection.add(
                documents=fulldocs ,
                ids=ids
            )

    # preprocessing_using_chat = f"""
    # Given the following chat history,
    # edit the user question to provide any information from the chat history that would be needed to make the last user question make sense out of context:
    # History: {}
    # Last Question: {question}
    # Edited Question:    
    # """
    preprocessing_without_context= f"""
    You are an assistant for question-answering tasks from a specific file.
    Use the following question to retrive infromation from it and give me 5 questions maxiumum you need to retrive from the file not from the user to be able to answer correctly.
    dont answer the question yet just ask about more information you need to know give me questions only number each one of them in new line.
    the question is:
    Question: {question} 
    """
    preprocessing_without_context2= f"""
    You are an assistant for question-answering tasks from a specific file.
    Use the following question to retrive infromation from it and give me 5 keywords maxiumum realted to the question to be able to answer correctly.
    dont answer the question yet just give the keyword that might give you more information you need to know to answer correctly.
    give me the keywords only do not talk at all
    the question is:
    Question: {question} 
    """

    response = client.chat('user',preprocessing_without_context2)

    context=""
    keywordList = response['message'].split("\n")
    for keywd in keywordList:
        results=collection.query(
        query_texts=[keywd],
        n_results=numofresults # how many results to return
        )
        for doc in results["documents"][0]:
            context+=doc+"\n"
    results = collection.query(
        query_texts=[question],
        n_results=numofresults # how many results to return
    )
    
    print(results)
    tmp =""
    for doc in results["documents"][0]:
        tmp+=doc+"\n"
    keywordContext=context
    QuestionContext = tmp
    QuestionAndKeyWordContext=context+"\n"+tmp
    
    template=f"""
    You are an assistant for question-answering tasks. 
    Use the following pieces of retrieved context to answer the question. 
    If you don't know the answer, just say that you don't know. 
    Use five sentence maximum and keep the answer concise.
    Question: {question} 
    Context: {QuestionAndKeyWordContext} 
    Answer:
    """
    templateArabic = f"""
    أنت مساعد لمهام الإجابة على الأسئلة. 
    استخدم الأجزاء التالية من السياق المسترجع للإجابة على السؤال. 
    إذا كنت لا تعرف الإجابة، فقط قل أنك لا تعرف. 
    استخدم جملة واحدة كحد أقصى واجعل الإجابة موجزة.
    ترجم مايلي الى العربية ومن ثم اجب
    السؤال هو {question}
    السياق هو :{QuestionAndKeyWordContext}
    الجواب باللغة العربية:
    """
    response = client.chat('user',template)
  
    collection.delete(ids=ids)
    return response
