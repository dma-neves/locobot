from langchain_core.documents import Document
from langchain_community.document_loaders.base import BaseLoader
from typing import List, Optional
from os import listdir
from os.path import isfile, join


class TextFileLoader(BaseLoader):
    """Loads text files."""

    def __init__(
        self,
        file_paths: List[str],
        encoding: Optional[str] = None,
    ):
        self.file_paths = file_paths
        self.encoding = encoding

    def load(self) -> List[Document]:

        docs = []
        for file_path in self.file_paths:
            try:
                with open(file_path, "r", encoding=self.encoding) as f:
                    content = f.read()
                metadata = {"source": file_path}
                doc = Document(page_content=content, metadata=metadata)
                docs.append(doc)
            except Exception as e:
                print(f"Error reading file '{file_path}': {e}")
        return docs