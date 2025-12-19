Create file: tower_generator.py
import os
 from openai import OpenAI
 from dotenv import load_dotenv
 from typing import List, Dict

 load_dotenv()

 class TowerGenerator:
 	"""Generate three-tower structure using LLM"""
 	
 	def __init__(self):
     	self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
 	
 	def generate_tower_1(self, query: str, contexts: List[str]) -> str:
     	"""Generate strategic insight (Tower 1)"""
     	
     	context_text = "\n\n".join([f"Context {i+1}:\n{ctx}"
                             	     for i, ctx in enumerate(contexts)])
     	
     	prompt = f"""Based on the following contexts, generate a strategic insight
 about: {query}

 {context_text}

 Requirements:
 - Exactly 50-75 words
 - Focus on strategic novelty and decision implications
 - Include temporal horizon (when this matters)
 - Action-oriented tone

 Generate only the insight, no preamble:"""

     	response = self.client.chat.completions.create(
             model="gpt-4o-mini",
         	messages=[
             	{"role": "system", "content": "You are a strategic foresight analyst."},
             	{"role": "user", "content": prompt}
         	],
         	temperature=0.7,
         	max_tokens=150
     	)
     	
     	return response.choices[0].message.content.strip()
 	
 	def generate_tower_2(self, tower_1: str, contexts: List[str]) -> List[Dict]:
     	"""Generate thematic contexts (Tower 2)"""
     	
     	themes_prompt = f"""Given this strategic insight:
 {tower_1}

 And these source contexts:
 {chr(10).join([f"Context {i+1}: {ctx[:300]}..." for i, ctx in enumerate(contexts)])}

 Generate 3 thematic context sections (each 200-300 words):
 1. Technology/Scientific Context
 2. Market/Economic Context 
 3. Strategic Implications Context

 Format as JSON array with structure:
 [
   {{"theme": "Technology Context", "content": "..."}},
   {{"theme": "Market Context", "content": "..."}},
   {{"theme": "Strategic Implications", "content": "..."}}
 ]

 Each context should explain and elaborate on the Tower 1 insight."""

         response = self.client.chat.completions.create(
             model="gpt-4o-mini",
         	messages=[
             	{"role": "system", "content": "You are a strategic analyst."},
             	{"role": "user", "content": themes_prompt}
         	],
         	temperature=0.7,
         	max_tokens=1200
     	)
     	
     	import json
     	return json.loads(response.choices[0].message.content)
 	
 	def format_tower_3(self, contexts: List[str], metadata: List[Dict]) -> List[Dict]:
     	"""Format source fragments (Tower 3)"""
     	
     	fragments = []
     	for i, (ctx, meta) in enumerate(zip(contexts, metadata)):
         	# Truncate to 400-600 characters
         	fragment_text = ctx[:550] + "..." if len(ctx) > 550 else ctx
         	
         	fragments.append({
             	'fragment_id': i + 1,
             	'text': fragment_text,
             	'source': meta.get('source', 'Unknown'),
             	'chunk_id': meta.get('chunk_id', 'N/A'),
        	     'char_count': len(fragment_text)
         	})
     	
     	return fragments

 # Usage example
 if __name__ == "__main__":
 	generator = TowerGenerator()
 	
 	sample_contexts = [
     	"Recent advances in perovskite solar cells show efficiency gains...",
     	"Market analysis indicates growing demand for renewable energy..."
 	]
 	
 	tower_1 = generator.generate_tower_1(
     	"emerging solar technologies",
     	sample_contexts
 	)
 	print("Tower 1:", tower_1)
