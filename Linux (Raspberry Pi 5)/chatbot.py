from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
import os.path
from Config import *

class Chatbot:
    def __init__(self, pdf_files:list, reset_vectorstore:bool):
        self.pdf_files = pdf_files
        self.reset_vectorstore = reset_vectorstore
        self.is_initialized = False

    def initialize(self):
        if not self.is_initialized:
            self.vectorstore = self._build_vectorstore()
            self.qa = self._build_qa(self.vectorstore)
            self.is_initialized = True

    def query(self, query):
        if not self.is_initialized:
            raise Exception("Bot not initialized yet")
        
        result = self.qa.invoke(query)
        
        response = result['result']

        return response
    
    def _build_vectorstore(self):
        vectorstore_file_name = "faiss_index_constitution"
    
        vectorstore_file_exists = os.path.exists(vectorstore_file_name)
    
        embeddings = OpenAIEmbeddings()
    
        if not vectorstore_file_exists or self.reset_vectorstore:
            documents = []            
            
            for pdf_file in self.pdf_files:
                if not os.path.exists(pdf_file):
                    raise Exception(f"File {pdf_file} does not exist")
                
                # Load document using PyPDFLoader document loader
                loader = PyPDFLoader(pdf_file)
                documents.extend(loader.load())
                
            # Split document in chunks
            text_splitter = CharacterTextSplitter(chunk_size=2000, chunk_overlap=50, separator="\n")

            docs = text_splitter.split_documents(documents=documents)
        
            # Create vectors
            vectorstore = FAISS.from_documents(docs, embeddings)
            
            # Persist the vectors locally on disk
            vectorstore.save_local(vectorstore_file_name)

        # Load from local storage
        persisted_vectorstore = FAISS.load_local(vectorstore_file_name, embeddings, allow_dangerous_deserialization=True)
    
        return persisted_vectorstore
    
    def _build_qa(self, persisted_vectorstore):
        # Define a custom prompt template

        prompt_template = """
        Your name is Smart Assistant. You are an intelligent and helpful AI assistant.
        Always refer to yourself as Smart Assistant.
        Keep your answers short and concise, no longer than 1 sentence.
        Use the following context to answer the user's question.
        If includes anything like, "nothing", say, "Ok cool!"
        If you don't know the answer, just say "sorry, I dont know how what you meant! Anything else I can help you with?" without ever making things up.
        Do not say, "can I assist you with?" or anything with "assist" in a sentence.
        If includes anything like, "bye" or "goodbye", say a nice goodbye comment without making things up.
        
        Context:
        {context}

        Question:
        {question}

        Helpful answer in markdown:
        """

        prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

        qa = RetrievalQA.from_chain_type(
            llm=OpenAI(),
            chain_type="stuff",
            retriever=persisted_vectorstore.as_retriever(),
            chain_type_kwargs={"prompt": prompt}
        )

        return qa

