from langchain_community.document_loaders import PyPDFLoader , TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

def check_file_type(file_path: str) -> str:
    # First check by extension
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".txt":
        return "text"
    elif ext == ".pdf":
        return "pdf"



class loader:
    def __init__(self, path : str ):
        self.path = path 
    
    def upload(self):

        check = check_file_type(self.path)
        if check == "text":
            load = TextLoader(file_path=self.path , encoding="utf-8" )
            return load.load()
        
        
        elif  check == "pdf":
            load = PyPDFLoader(file_path=self.path )
            return load.load()
    



class chunker:
    
    def __init__(self, text: str):
        self.text = text

    def split(self, chunk_size: int, chunk_overlap: int = 0):
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        return splitter.split_text(self.text)

    def splitter_for_embedding(self):
        return self.split(chunk_size=2000, chunk_overlap=100)

    def splitter_for_summary(self):
        return self.split(chunk_size=10000, chunk_overlap=0)
