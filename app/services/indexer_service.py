from typing import Dict, List
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.document_loaders import UnstructuredURLLoader

def index(urls: List[str]):
    try:
        loader = UnstructuredURLLoader(urls=urls)
        documents = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        docs = text_splitter.split_documents(documents)

        embeddings = OpenAIEmbeddings()
        persist_directory = 'db'

        db = Chroma.from_documents(documents=docs, embedding=embeddings, persist_directory=persist_directory)
        db.persist()
        
        return "success", f"処理が正常に完了しました。"

    except Exception as e:
        return "error", str(e)

