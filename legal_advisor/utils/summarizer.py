from langchain.chains.summarize import load_summarize_chain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.docstore.document import Document
from dotenv import load_dotenv
import os 

load_dotenv()


class summary :

    def __init__(self , docs: list ,  api: str = None):
        self.docs = docs 
        self.google_api_key = api or os.getenv("GOOGLE_API_KEY") 
    
    def caller(self):
        model = ChatGoogleGenerativeAI(
            model = "gemini-2.5-flash-lite",
            google_api_key = self.google_api_key)
      
        summary_chain = load_summarize_chain(model, chain_type="map_reduce")

        summary_docs = [Document(page_content=chunk) for chunk in self.docs]

        summary = summary_chain.run(summary_docs)

        return summary