# pip install sentence-transformers scikit-learn
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
import numpy as np

embedder = SentenceTransformer("all-MiniLM-L6-v2")

def cluster_snippets(snippets: List[str], k: int = 8) -> Dict[int, List[str]]:
    X = embedder.encode(snippets, normalize_embeddings=True)
    km = KMeans(n_clusters=k, random_state=42, n_init="auto")
    labels = km.fit_predict(X)
    clusters = {}
    for s, lab in zip(snippets, labels):
        clusters.setdefault(int(lab), []).append(s)
    return clusters

snippets = [
    "Urea electrolysis improves hydrogen yield using wastewater streams.",
    "Cultivated meat bioreactors reduce emissions compared to livestock systems.",
    "Agrophotovoltaic systems enable dual land-use for crops and solar power.",
    "PFAS removal via catalytic oxidation reduces persistent pollutants in soil.",
    # ... add more snippets from documents, patents, abstracts
]

clusters = cluster_snippets(snippets, k=3)
print(clusters)
