Create file: vector_store.py
from sentence_transformers import SentenceTransformer
 import chromadb
 from typing import List, Dict

 class VectorStore:
 	"""Manage document embeddings and similarity search"""
 	
 	def __init__(self, collection_name: str = "foresight_docs"):
     	# Initialize embedding model (local, no API needed)
     	self.model = SentenceTransformer('all-MiniLM-L6-v2')
     	
     	# Initialize ChromaDB
     	self.client = chromadb.Client()
     	self.collection = self.client.get_or_create_collection(
         	name=collection_name,
             metadata={"description": "Foresight document embeddings"}
     	)
 	
 	def add_documents(self, documents: List[Dict]):
     	"""Add document chunks to vector store"""
     	texts = [doc['text'] for doc in documents]
     	embeddings = self.model.encode(texts)
     	
     	# Add to ChromaDB
     	self.collection.add(
             embeddings=embeddings.tolist(),
         	documents=texts,
         	metadatas=[{
             	'source': doc.get('source', 'unknown'),
             	'chunk_id': str(i)
         	} for i, doc in enumerate(documents)],
         	ids=[f"doc_{i}" for i in range(len(documents))]
     	)
 	
 	def search(self, query: str, n_results: int = 5) -> List[Dict]:
     	"""Semantic search for relevant chunks"""
     	query_embedding = self.model.encode([query])[0]
     	
     	results = self.collection.query(
             query_embeddings=[query_embedding.tolist()],
         	n_results=n_results
     	)
         
     	# Format results
     	formatted_results = []
     	for i in range(len(results['documents'][0])):
         	formatted_results.append({
             	'text': results['documents'][0][i],
             	'metadata': results['metadatas'][0][i],
             	'distance': results['distances'][0][i]
         	})
     	
     	return formatted_results

 # Usage example
 if __name__ == "__main__":
 	store = VectorStore()
 	
 	# Example: add sample documents
 	sample_docs = [
   	  {'text': 'Sample text about renewable energy...', 'source': 'doc1.pdf'},
     	{'text': 'More content about solar technology...', 'source': 'doc2.pdf'}
 	]
 	store.add_documents(sample_docs)
 	
 	# Search
 	results = store.search("solar energy innovations", n_results=3)
 	for result in results:
     	print(f"Distance: {result['distance']:.3f}")
     	print(f"Text: {result['text'][:100]}...")
