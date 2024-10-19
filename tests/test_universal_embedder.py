import unittest
from universal_embedder import extractor, embedder, vectordb, utils
import os

class TestUniversalEmbedder(unittest.TestCase):

    def test_extract_text_from_pdf(self):
        pdf_path = 'tests/sample.pdf'  # Add your pdf in the tests directory
        if os.path.exists(pdf_path):
            text = extractor.extract_text_from_pdf(pdf_path)
            self.assertIsInstance(text, str)
        else:
            self.skipTest("sample.pdf not found")

    def test_generate_embeddings(self):
        text = "This is a test sentence."
        embedding = embedder.generate_embeddings(text)
        self.assertIsNotNone(embedding)
        self.assertEqual(len(embedding), 384)

    def test_store_embedding_in_vectordb(self):
        embedding = [0.0] * 384  # Mock embedding
        metadata = {'name': 'test', 'type': 'test'}
        vectordb.store_embedding_in_vectordb(embedding, metadata)
        # Since we can't retrieve from Pinecone in tests, we assume it passes if no exception

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
