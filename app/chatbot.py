"""
Core chatbot module for answering questions about the thesis.
"""

import numpy as np
import anthropic
from typing import List, Tuple
from .config import settings
from .data_processor import ThesisDataProcessor

class ThesisChatbot:
    def __init__(self):
        self.data_processor = ThesisDataProcessor()
        self.chunks = None
        self.embeddings = None
        self.embedding_model = None
        self.anthropic_client = None
        self._initialize_client()
        
    def _initialize_client(self):
        """Initialize the Anthropic client."""
        if not settings.anthropic_api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment variables")
        
        try:
            self.anthropic_client = anthropic.Anthropic(api_key=settings.anthropic_api_key)
        except Exception as e:
            raise ValueError(f"Failed to initialize Anthropic client: {e}")
    
    def load_data(self):
        """Load processed chunks and embeddings."""
        if self.chunks is None or self.embeddings is None:
            print("Loading thesis data...")
            self.chunks, self.embeddings = self.data_processor.load_processed_data()
            self.embedding_model = self.data_processor.load_embedding_model()
    
    def find_most_similar_chunks(self, question_embedding: np.ndarray, top_k: int = None) -> List[int]:
        """
        Find the top_k most similar chunks to a question embedding.
        """
        if top_k is None:
            top_k = settings.top_k_chunks
            
        # Calculate cosine similarity between the question embedding and all chunk embeddings
        similarities = np.dot(self.embeddings, question_embedding) / (
            np.linalg.norm(self.embeddings, axis=1) * np.linalg.norm(question_embedding)
        )
        
        # Get the indices of the top_k most similar chunks
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        
        return top_indices.tolist()
    
    def find_relevant_chunks_with_threshold(self, question_embedding: np.ndarray, similarity_threshold: float = 0.75) -> List[int]:
        """
        Find all chunks with a similarity score above a certain threshold.
        """
        # Calculate cosine similarity
        similarities = np.dot(self.embeddings, question_embedding) / (
            np.linalg.norm(self.embeddings, axis=1) * np.linalg.norm(question_embedding)
        )
        
        # Find all indices where the similarity is above the threshold
        relevant_indices = np.where(similarities > similarity_threshold)[0]
        
        # Sort them by similarity score to present the most relevant ones first
        relevant_indices = relevant_indices[np.argsort(similarities[relevant_indices])[::-1]]
        
        return relevant_indices.tolist()
    
    def generate_answer(self, question: str, context: str) -> str:
        """
        Generate an answer using the Anthropic API.
        """
        prompt = f"""You are an expert research assistant answering questions about a PhD thesis. 
Your task is to answer the user's question based ONLY on the provided context below.
If the context does not contain the answer, you must state that you cannot find the answer in the document.

CONTEXT FROM THESIS:
---
{context}
---

USER'S QUESTION: {question}

ANSWER:"""

        try:
            response = self.anthropic_client.messages.create(
                model="claude-3-5-haiku-20241022",
                max_tokens=settings.max_tokens,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response.content[0].text
        except Exception as e:
            return f"Sorry, I encountered an error trying to generate an answer: {e}"
    
    def answer_question(self, question: str, use_threshold: bool = False, similarity_threshold: float = 0.75) -> dict:
        """
        Main method to answer a question about the thesis.
        
        Args:
            question: The user's question
            use_threshold: Whether to use similarity threshold instead of top_k
            similarity_threshold: Minimum similarity score for relevant chunks
            
        Returns:
            dict containing the answer and metadata
        """
        # Ensure data is loaded
        self.load_data()
        
        # Embed the user's question
        question_embedding = self.embedding_model.encode(question)
        
        # Find relevant chunks
        if use_threshold:
            relevant_chunk_indices = self.find_relevant_chunks_with_threshold(
                question_embedding, similarity_threshold
            )
        else:
            relevant_chunk_indices = self.find_most_similar_chunks(question_embedding)
        
        if not relevant_chunk_indices:
            return {
                "answer": "I couldn't find any relevant information in the thesis to answer your question.",
                "num_chunks_used": 0,
                "chunk_indices": []
            }
        
        # Create context from relevant chunks
        context = "\n\n---\n\n".join([self.chunks[i] for i in relevant_chunk_indices])
        
        # Generate answer
        answer = self.generate_answer(question, context)
        
        return {
            "answer": answer,
            "num_chunks_used": len(relevant_chunk_indices),
            "chunk_indices": relevant_chunk_indices
        } 