"""
Data processing module for converting thesis PDF to chunks and embeddings.
This module handles the one-time data preparation step.
"""

import os
import pickle
import pymupdf4llm
import numpy as np
from langchain.text_splitter import MarkdownTextSplitter
from sentence_transformers import SentenceTransformer
from typing import List, Tuple
from .config import settings

class ThesisDataProcessor:
    def __init__(self):
        self.embedding_model = None
        self.chunks_file = os.path.join(settings.chunks_path, "thesis_chunks.pkl")
        self.embeddings_file = os.path.join(settings.embeddings_path, "thesis_embeddings.pkl")
        
    def load_embedding_model(self):
        """Load the sentence transformer model."""
        if self.embedding_model is None:
            print(f"Loading embedding model: {settings.embedding_model}")
            self.embedding_model = SentenceTransformer(settings.embedding_model)
        return self.embedding_model
    
    def pdf_to_markdown(self, pdf_path: str) -> str:
        """Convert PDF to markdown text."""
        print(f"Converting PDF to markdown: {pdf_path}")
        md_text = pymupdf4llm.to_markdown(pdf_path)
        return md_text
    
    def load_markdown_from_url(self, url: str) -> str:
        """Load markdown text from a URL (for deployment)."""
        import requests
        print(f"Downloading markdown from: {url}")
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    
    def chunk_text(self, text: str) -> List[str]:
        """Split text into chunks using Langchain's MarkdownTextSplitter."""
        print(f"Splitting text into chunks (size: {settings.chunk_size}, overlap: {settings.chunk_overlap})")
        splitter = MarkdownTextSplitter(
            chunk_size=settings.chunk_size, 
            chunk_overlap=settings.chunk_overlap
        )
        documents = splitter.create_documents([text])
        chunks = [doc.page_content for doc in documents]
        print(f"Created {len(chunks)} chunks")
        return chunks
    
    def create_embeddings(self, chunks: List[str]) -> np.ndarray:
        """Create embeddings for text chunks."""
        model = self.load_embedding_model()
        print(f"Generating embeddings for {len(chunks)} chunks...")
        embeddings = model.encode(chunks, show_progress_bar=True)
        print(f"Embeddings shape: {embeddings.shape}")
        return embeddings
    
    def save_processed_data(self, chunks: List[str], embeddings: np.ndarray):
        """Save chunks and embeddings to disk."""
        # Ensure directories exist
        os.makedirs(settings.chunks_path, exist_ok=True)
        os.makedirs(settings.embeddings_path, exist_ok=True)
        
        # Save chunks
        with open(self.chunks_file, 'wb') as f:
            pickle.dump(chunks, f)
        print(f"Saved chunks to {self.chunks_file}")
        
        # Save embeddings
        with open(self.embeddings_file, 'wb') as f:
            pickle.dump(embeddings, f)
        print(f"Saved embeddings to {self.embeddings_file}")
    
    def load_processed_data(self) -> Tuple[List[str], np.ndarray]:
        """Load chunks and embeddings from disk."""
        if not os.path.exists(self.chunks_file) or not os.path.exists(self.embeddings_file):
            raise FileNotFoundError("Processed data not found. Please run data preparation first.")
        
        with open(self.chunks_file, 'rb') as f:
            chunks = pickle.load(f)
        
        with open(self.embeddings_file, 'rb') as f:
            embeddings = pickle.load(f)
        
        print(f"Loaded {len(chunks)} chunks and embeddings with shape {embeddings.shape}")
        return chunks, embeddings
    
    def process_thesis(self, pdf_path: str = None, markdown_url: str = None) -> Tuple[List[str], np.ndarray]:
        """Complete pipeline to process thesis from PDF to embeddings."""
        
        # Check if processed data already exists
        if os.path.exists(self.chunks_file) and os.path.exists(self.embeddings_file):
            print("Processed data already exists. Loading from disk...")
            return self.load_processed_data()
        
        # Process from scratch
        print("Processing thesis...")
        
        # Get markdown text - try markdown first, then PDF
        markdown_file = os.path.join(settings.raw_data_path, "thesis.md")
        
        if os.path.exists(markdown_file):
            # Use existing markdown file
            print(f"Loading markdown from: {markdown_file}")
            with open(markdown_file, 'r', encoding='utf-8') as f:
                md_text = f.read()
        elif markdown_url:
            # For deployment - download from URL
            md_text = self.load_markdown_from_url(markdown_url)
        elif pdf_path and os.path.exists(pdf_path):
            # Local development - convert PDF
            md_text = self.pdf_to_markdown(pdf_path)
        else:
            # Try default PDF path as fallback
            default_pdf = os.path.join(settings.raw_data_path, "thesis.pdf")
            if os.path.exists(default_pdf):
                md_text = self.pdf_to_markdown(default_pdf)
            else:
                raise FileNotFoundError(
                    "No thesis source found. Please provide thesis.md, thesis.pdf, "
                    "or specify pdf_path/markdown_url parameters."
                )
        
        # Chunk the text
        chunks = self.chunk_text(md_text)
        
        # Create embeddings
        embeddings = self.create_embeddings(chunks)
        
        # Save processed data
        self.save_processed_data(chunks, embeddings)
        
        return chunks, embeddings 