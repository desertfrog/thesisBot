"""
Core chatbot module for answering questions about the thesis.
"""

import numpy as np
import anthropic
import pickle
import os
import voyageai
from typing import List, Tuple
from .config import settings


class ThesisChatbot:
    def __init__(self):
        self.chunks = []
        self.embeddings = None
        self.voyage_client = None
        self.anthropic_client = None
        self._initialize_clients()
        
    def _initialize_clients(self):
        """Initialize the API clients."""
        if not settings.anthropic_api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment variables")
        
        try:
            self.anthropic_client = anthropic.Anthropic(api_key=settings.anthropic_api_key)
        except Exception as e:
            raise ValueError(f"Failed to initialize Anthropic client: {e}")
            
        # Initialize Voyage AI client
        if settings.voyage_api_key:
            self.voyage_client = voyageai.Client(api_key=settings.voyage_api_key)
        else:
            self.voyage_client = voyageai.Client()  # Will use VOYAGE_API_KEY env var
        
    def load_data(self):
        """Load processed chunks and embeddings."""
        chunks_file = os.path.join(settings.chunks_path, "thesis_chunks.pkl")
        embeddings_file = os.path.join(settings.embeddings_path, "thesis_embeddings.pkl")
        
        if not os.path.exists(chunks_file) or not os.path.exists(embeddings_file):
            raise FileNotFoundError("Processed data not found. Please run data preparation first.")
        
        # Load chunks
        with open(chunks_file, 'rb') as f:
            self.chunks = pickle.load(f)
        
        # Load embeddings
        with open(embeddings_file, 'rb') as f:
            self.embeddings = pickle.load(f)
        
        print(f"Loaded {len(self.chunks)} chunks and embeddings with shape {self.embeddings.shape}")
    
    def find_most_similar_chunks(self, question: str, top_k: int = None) -> List[int]:
        """
        Find the top_k most similar chunks to a question.
        """
        if top_k is None:
            top_k = settings.top_k_chunks
            
        # Generate embedding for the question using Voyage AI
        result = self.voyage_client.embed(
            texts=[question],
            model=settings.embedding_model,
            input_type="query"  # This is a query for retrieval
        )
        question_embedding = np.array(result.embeddings[0])
        
        # Calculate cosine similarity between the question embedding and all chunk embeddings
        similarities = np.dot(self.embeddings, question_embedding) / (
            np.linalg.norm(self.embeddings, axis=1) * np.linalg.norm(question_embedding)
        )
        
        # Get the indices of the top_k most similar chunks
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        
        return top_indices.tolist()
    
    def find_relevant_chunks_with_threshold(self, question: str, similarity_threshold: float = 0.75) -> List[int]:
        """
        Find all chunks with a similarity score above a certain threshold.
        """
        # Generate embedding for the question using Voyage AI
        result = self.voyage_client.embed(
            texts=[question],
            model=settings.embedding_model,
            input_type="query"  # This is a query for retrieval
        )
        question_embedding = np.array(result.embeddings[0])
        
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
        Generate an answer using Claude based on the question and context.
        """
        system_prompt = """You are a helpful assistant that answers questions based on the provided context from a thesis document. 
        
        Guidelines:
        - Answer only based on the information provided in the context
        - If the context doesn't contain enough information to answer the question, say so clearly
        - Be concise but comprehensive in your responses
        - Cite specific parts of the context when relevant
        - If asked about topics not covered in the context, explain that the information is not available in the provided thesis content
        """
        
        user_prompt = f"""Context from thesis:
        {context}
        
        Question: {question}
        
        Please provide a comprehensive answer based on the context above."""

        try:
            response = self.anthropic_client.messages.create(
                model="claude-3-5-haiku-20241022",
                max_tokens=settings.max_tokens,
                system=system_prompt,
                messages=[
                    {"role": "user", "content": user_prompt}
                ]
            )
            return response.content[0].text
        except Exception as e:
            return f"Error generating response: {str(e)}"
    
    def answer_question(self, question: str, use_threshold: bool = False, similarity_threshold: float = 0.75, top_k: int = None):
        """
        Answer a question using the thesis content.
        
        Args:
            question: The question to answer
            use_threshold: Whether to use similarity threshold instead of top-k
            similarity_threshold: Minimum similarity score for relevant chunks
            top_k: Number of chunks to retrieve (overrides settings if provided)
        """
        if self.chunks is None or self.embeddings is None:
            return {"error": "Data not loaded. Please load the processed thesis data first."}
        
        # Use provided top_k or fall back to default (equivalent to 5% of 365 chunks)
        k = top_k if top_k is not None else 18  # 5% of 365 chunks as default
        
        # Find relevant chunks
        if use_threshold:
            relevant_chunk_indices = self.find_relevant_chunks_with_threshold(
                question, similarity_threshold
            )
        else:
            # Update the method call to use our k value
            relevant_chunk_indices = self.find_most_similar_chunks(question, top_k=k)
        
        if not relevant_chunk_indices:
            return {
                "answer": "I couldn't find any relevant information in the thesis to answer your question.",
                "num_chunks_used": 0,
                "chunk_indices": []
            }
        
        # Create context from relevant chunks
        context = "\n\n---\n\n".join([self.chunks[i]['content'] for i in relevant_chunk_indices])
        
        # Generate answer
        answer = self.generate_answer(question, context)
        
        return {
            "answer": answer,
            "num_chunks_used": len(relevant_chunk_indices),
            "chunk_indices": relevant_chunk_indices
        } 