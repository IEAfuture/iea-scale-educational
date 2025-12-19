Create file: main.py
from document_processor import DocumentProcessor
 from vector_store import VectorStore
 from tower_generator import TowerGenerator
 import json
 from pathlib import Path

 class WeakSignalSystem:
 	"""Complete weak signal intelligence system"""
 	
 	def __init__(self):
     	self.processor = DocumentProcessor()
     	self.store = VectorStore()
     	self.generator = TowerGenerator()
 	
 	def ingest_documents(self, pdf_directory: str):
     	"""Process and store all PDFs in directory"""
     	pdf_files = list(Path(pdf_directory).glob("*.pdf"))
     	
     	print(f"Processing {len(pdf_files)} documents...")
     	all_chunks = []
     	
     	for pdf_file in pdf_files:
         	result = self.processor.process_document(str(pdf_file))
         	
         	# Add source metadata to chunks
         	for chunk in result['chunks']:
             	chunk['source'] = result['source']
         	
             all_chunks.extend(result['chunks'])
     	
     	self.store.add_documents(all_chunks)
     	print(f"Added {len(all_chunks)} chunks to vector store")
 	
 	def analyze_signal(self, query: str, n_contexts: int = 5) -> Dict:
     	"""Complete analysis: query → three towers"""
     	
     	# Step 1: Retrieve relevant contexts
     	search_results = self.store.search(query, n_results=n_contexts)
     	contexts = [r['text'] for r in search_results]
     	metadata = [r['metadata'] for r in search_results]
     	
     	# Step 2: Generate Tower 1
     	print("Generating strategic insight...")
     	tower_1 = self.generator.generate_tower_1(query, contexts)
     	
     	# Step 3: Generate Tower 2
     	print("Generating thematic contexts...")
     	tower_2 = self.generator.generate_tower_2(tower_1, contexts)
     	
     	# Step 4: Format Tower 3
     	print("Formatting evidence fragments...")
     	tower_3 = self.generator.format_tower_3(contexts, metadata)
     	
     	# Assemble complete analysis
     	return {
         	'query': query,
   	      'tower_1': {
             	'insight': tower_1,
             	'word_count': len(tower_1.split())
         	},
         	'tower_2': tower_2,
         	'tower_3': tower_3,
         	'metadata': {
             	'sources_consulted': len(set(m['source'] for m in metadata)),
             	'contexts_retrieved': len(contexts)
         	}
     	}
 	
 	def save_analysis(self, analysis: Dict, output_file: str):
     	"""Save analysis to JSON file"""
     	with open(output_file, 'w', encoding='utf-8') as f:
         	json.dump(analysis, f, indent=2, ensure_ascii=False)

 # Main execution
 if __name__ == "__main__":
 	system = WeakSignalSystem()
 	
 	# Step 1: Ingest documents (run once)
     system.ingest_documents("data/")
 	
 	# Step 2: Analyze weak signal
 	query = "What are emerging developments in biodegradable electronics?"
 	analysis = system.analyze_signal(query)
 	
 	# Step 3: Display results
 	print("\n" + "="*60)
 	print("TOWER 1 - STRATEGIC INSIGHT")
 	print("="*60)
 	print(analysis['tower_1']['insight'])
 	
 	print("\n" + "="*60)
 	print("TOWER 2 - THEMATIC CONTEXTS")
 	print("="*60)
 	for theme in analysis['tower_2']:
         print(f"\n{theme['theme']}:")
     	print(theme['content'][:200] + "...")
 	
 	print("\n" + "="*60)
 	print(f"TOWER 3 - DOCUMENTARY FRAGMENTS ({len(analysis['tower_3'])} fragments)")
 	print("="*60)
 	for frag in analysis['tower_3'][:2]:  # Show first 2
     	print(f"\nFragment {frag['fragment_id']} from {frag['source']}:")
     	print(frag['text'][:150] + "...")
 	
 	# Save complete analysis
 	system.save_analysis(analysis, "outputs/analysis.json")
 	print("\nComplete analysis saved to outputs/analysis.json")



Complete working code with additional features (web interface, visualization) available in the course repository.

