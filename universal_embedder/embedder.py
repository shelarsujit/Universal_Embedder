from sentence_transformers import SentenceTransformer
import traceback

# Load the SentenceTransformer Model for generating embeddings
try:
    model = SentenceTransformer('all-MiniLM-L6-v2')
except Exception as e:
    print(f"Error loading SentenceTransformer model: {e}")
    traceback.print_exc()
    model = None

def generate_embeddings(text):
    if model:
        try:
            return model.encode(text)
        except Exception as e:
            print(f"Error generating embeddings: {e}")
            traceback.print_exc()
            return None
    else:
        print("Model not loaded.")
        return None
