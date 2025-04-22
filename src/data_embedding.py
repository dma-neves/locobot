import os
import ollama

__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import chromadb

from text_file_loader import TextFileLoader


def list_files(directory, include_extensions=None, exclude_paths=None):
    
    file_paths = []
    
    # lower case the extensions
    if include_extensions:
        include_extensions = [ext.lower() for ext in include_extensions]
    
    # convert paths to absolute paths
    if exclude_paths:
        exclude_paths = [os.path.abspath(path) if not os.path.isabs(path) else path for path in exclude_paths]

    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            abs_file_path = os.path.abspath(file_path)
            
            if exclude_paths and any(abs_file_path.startswith(excluded) or abs_file_path == excluded for excluded in exclude_paths):
                continue

            if include_extensions and os.path.splitext(filename)[1].lower() not in include_extensions:
                continue
                
            file_paths.append(file_path)
    
    return file_paths
    

def load_data(file_paths):
    
    loader = TextFileLoader(file_paths)
    files = loader.load()
    collection = chromadb.Client().create_collection(name="locobot_files")
    
    # store each file in a vector embedding database
    for i, file in enumerate(files):
        response = ollama.embeddings(model="mxbai-embed-large", prompt=file.__str__())
        embedding = response["embedding"]
        collection.add(
            ids=[str(i)],
            embeddings=[embedding],
            documents=[file.__str__()]
        )
        
    return collection
    
def get_embedding_data(collection, prompt: str):

  response = ollama.embeddings(
    prompt=prompt,
    model="mxbai-embed-large"
  )
  results = collection.query(
    query_embeddings=[response["embedding"]],
    n_results=20
  )

  return results['documents']