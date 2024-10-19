import pinecone
from .config import load_config
import traceback

config = load_config()
pinecone_api_key = config['pinecone']['api_key']
pinecone_environment = config['pinecone']['environment']
index_name = config['index']['name']
dimension = config['index']['dimension']
metric = config['index']['metric']

# Initialize Pinecone
try:
    pinecone.init(api_key=pinecone_api_key, environment=pinecone_environment)
    if index_name not in pinecone.list_indexes():
        pinecone.create_index(name=index_name, dimension=dimension, metric=metric)
    index = pinecone.Index(index_name)
except Exception as e:
    print(f"Error initializing Pinecone: {e}")
    traceback.print_exc()
    index = None

def store_embedding_in_vectordb(embedding, metadata):
    if index and embedding is not None:
        try:
            vector = {
                'id': metadata['name'],
                'values': embedding.tolist(),
                'metadata': metadata
            }
            index.upsert(vectors=[vector])
            print(f"Stored embedding for {metadata['name']}")
        except Exception as e:
            print(f"Error storing embedding in Pinecone: {e}")
            traceback.print_exc()
    else:
        print("Index not initialized or embedding is None.")
