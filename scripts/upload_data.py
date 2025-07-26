#!/usr/bin/env python3
"""
Upload thesis data to a simple file sharing service for Render deployment.
This script uploads the processed chunks and embeddings so Render can download them.
"""

import os
import sys
import pickle
import base64
import json

# Add the app directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def create_data_package():
    """Create a JSON package with the processed data."""
    
    chunks_file = "data/chunks/thesis_chunks.pkl"
    embeddings_file = "data/embeddings/thesis_embeddings.pkl"
    
    if not os.path.exists(chunks_file) or not os.path.exists(embeddings_file):
        print("❌ Processed data not found. Please run 'python scripts/prepare_data.py' first.")
        return None
    
    print("📦 Loading processed data...")
    
    # Load chunks
    with open(chunks_file, 'rb') as f:
        chunks = pickle.load(f)
    
    # Load embeddings  
    with open(embeddings_file, 'rb') as f:
        embeddings = pickle.load(f)
    
    print(f"✅ Loaded {len(chunks)} chunks and embeddings with shape {embeddings.shape}")
    
    # Package data
    data_package = {
        "chunks": chunks,
        "embeddings": embeddings.tolist(),  # Convert numpy array to list
        "embeddings_shape": list(embeddings.shape)
    }
    
    # Save as JSON file
    output_file = "thesis_data_package.json"
    print(f"💾 Saving data package to {output_file}...")
    
    with open(output_file, 'w') as f:
        json.dump(data_package, f)
    
    print(f"✅ Data package created: {output_file}")
    print(f"📊 File size: {os.path.getsize(output_file) / 1024 / 1024:.1f} MB")
    
    return output_file

if __name__ == "__main__":
    create_data_package() 