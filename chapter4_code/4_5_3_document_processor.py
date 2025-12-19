Create file: document_processor.py
import PyPDF2
 from pathlib import Path
 from typing import List, Dict

 class DocumentProcessor:
 	"""Extract and chunk text from PDF documents"""
 	
 	def __init__(self, chunk_size: int = 1000, overlap: int = 200):
     	self.chunk_size = chunk_size
     	self.overlap = overlap
 	
 	def extract_text_from_pdf(self, pdf_path: str) -> str:
     	"""Extract all text from PDF file"""
     	text = ""
     	with open(pdf_path, 'rb') as file:
         	pdf_reader = PyPDF2.PdfReader(file)
   	      for page in pdf_reader.pages:
             	text += page.extract_text() + "\n"
     	return text
 	
 	def chunk_text(self, text: str) -> List[Dict]:
     	"""Split text into overlapping chunks with metadata"""
     	words = text.split()
     	chunks = []
     	
     	for i in range(0, len(words), self.chunk_size - self.overlap):
         	chunk_words = words[i:i + self.chunk_size]
         	chunk_text = ' '.join(chunk_words)
         	
         	chunks.append({
           	  'text': chunk_text,
             	'start_word': i,
             	'end_word': i + len(chunk_words),
             	'word_count': len(chunk_words)
         	})
     	
     	return chunks
 	
 	def process_document(self, pdf_path: str) -> Dict:
     	"""Complete processing pipeline"""
     	text = self.extract_text_from_pdf(pdf_path)
     	chunks = self.chunk_text(text)
     	
     	return {
         	'source': Path(pdf_path).name,
         	'full_text': text,
         	'chunks': chunks,
         	'chunk_count': len(chunks)
     	}

 # Usage example
 if __name__ == "__main__":
 	processor = DocumentProcessor(chunk_size=800, overlap=150)
 	result = processor.process_document("data/sample_paper.pdf")
 	print(f"Processed {result['chunk_count']} chunks from {result['source']}")
