"""
Data processing module for converting thesis PDF to chunks and embeddings.
This module handles the one-time data preparation step.
"""

import os
import pickle
import requests
from typing import List, Optional
import pymupdf4llm
from langchain.text_splitter import MarkdownTextSplitter
import numpy as np
import voyageai
from .config import settings


class ThesisDataProcessor:
    def __init__(self):
        self.raw_data_path = settings.raw_data_path
        self.chunks_path = settings.chunks_path
        self.embeddings_path = settings.embeddings_path
        self.chunks_file = os.path.join(self.chunks_path, "thesis_chunks.pkl")
        self.embeddings_file = os.path.join(self.embeddings_path, "thesis_embeddings.pkl")
        
        # Initialize Voyage AI client
        if settings.voyage_api_key:
            self.voyage_client = voyageai.Client(api_key=settings.voyage_api_key)
        else:
            self.voyage_client = voyageai.Client()  # Will use VOYAGE_API_KEY env var
        
        # Create directories
        os.makedirs(self.raw_data_path, exist_ok=True)
        os.makedirs(self.chunks_path, exist_ok=True)
        os.makedirs(self.embeddings_path, exist_ok=True)
    
    def pdf_to_markdown(self, pdf_path: str) -> str:
        """Convert PDF to markdown text."""
        print(f"Converting PDF to markdown: {pdf_path}")
        md_text = pymupdf4llm.to_markdown(pdf_path)
        return md_text
    
    def load_markdown_from_url(self, url: str) -> str:
        """Download markdown from URL."""
        print(f"Downloading markdown from: {url}")
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    
    def create_chunks(self, text: str) -> List[dict]:
        """Split text into chunks using MarkdownTextSplitter."""
        print(f"Splitting text into chunks (size: {settings.chunk_size}, overlap: {settings.chunk_overlap})")
        
        # Initialize the text splitter
        text_splitter = MarkdownTextSplitter(
            chunk_size=settings.chunk_size,
            chunk_overlap=settings.chunk_overlap
        )
        
        # Split the text
        chunks = text_splitter.split_text(text)
        print(f"Created {len(chunks)} chunks")
        
        # Convert to list of dicts with metadata
        chunk_dicts = []
        for i, chunk in enumerate(chunks):
            chunk_dict = {
                'index': i,
                'content': chunk,
                'length': len(chunk)
            }
            chunk_dicts.append(chunk_dict)
        
        return chunk_dicts
    
    def generate_embeddings(self, chunks: List[dict]) -> np.ndarray:
        """Generate embeddings using Voyage AI API."""
        print(f"Generating embeddings using Voyage AI model: {settings.embedding_model}")
        
        # Extract text content from chunks
        texts = [chunk['content'] for chunk in chunks]
        
        print(f"Generating embeddings for {len(texts)} chunks...")
        
        # Generate embeddings using Voyage AI
        result = self.voyage_client.embed(
            texts=texts,
            model=settings.embedding_model,
            input_type="document"  # These are documents for retrieval
        )
        
        # Convert to numpy array
        embeddings = np.array(result.embeddings)
        print(f"Embeddings shape: {embeddings.shape}")
        
        return embeddings
    
    def save_data(self, chunks: List[dict], embeddings: np.ndarray):
        """Save chunks and embeddings to files."""
        with open(self.chunks_file, 'wb') as f:
            pickle.dump(chunks, f)
        print(f"Saved chunks to {self.chunks_file}")
        
        with open(self.embeddings_file, 'wb') as f:
            pickle.dump(embeddings, f)
        print(f"Saved embeddings to {self.embeddings_file}")
    
    def load_processed_data(self):
        """Load processed chunks and embeddings."""
        with open(self.chunks_file, 'rb') as f:
            chunks = pickle.load(f)
        
        with open(self.embeddings_file, 'rb') as f:
            embeddings = pickle.load(f)
        
        return chunks, embeddings
    
    def process_thesis(self, pdf_path: str = None, markdown_url: str = None):
        """
        Process thesis into chunks and embeddings.
        
        Args:
            pdf_path: Path to PDF file (optional)
            markdown_url: URL to download markdown (optional)
        """
        # Check if data already exists
        if os.path.exists(self.chunks_file) and os.path.exists(self.embeddings_file):
            print("Processed data already exists. Skipping processing.")
            return
        
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
        elif pdf_path:
            # Convert PDF to markdown
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
        
        # Create chunks
        chunks = self.create_chunks(md_text)
        
        # Generate embeddings
        embeddings = self.generate_embeddings(chunks)
        
        # Save data
        self.save_data(chunks, embeddings) 