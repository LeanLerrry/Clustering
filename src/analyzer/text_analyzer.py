import os  # Add this import
import numpy as np
import pandas as pd
import torch
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from typing import Dict, List, Tuple
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache

class TextAnalyzer:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)
        
    def analyze_texts(self, texts, threshold=0.5, batch_size=500):
        # Convert texts to embeddings
        embeddings = self.model.encode(texts, batch_size=batch_size)
        
        # Calculate similarity matrix
        similarity_matrix = cosine_similarity(embeddings)
        
        # Create clusters with indices
        clusters = []
        processed = set()
        topic_number = 1
        
        for i in range(len(texts)):
            if i in processed:
                continue
                
            similar_indices = np.where(similarity_matrix[i] >= threshold)[0]
            cluster = {
                'topic_number': topic_number,
                'texts': [texts[idx] for idx in similar_indices],
                'indices': [int(idx) for idx in similar_indices]
            }
            clusters.append(cluster)
            processed.update(similar_indices)
            topic_number += 1
            
        return clusters
