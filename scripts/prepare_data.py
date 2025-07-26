#!/usr/bin/env python3
"""
Data preparation script for the thesis chatbot.
Run this script once to process your thesis PDF into chunks and embeddings.

Usage:
    python scripts/prepare_data.py [path_to_thesis.pdf]
"""

import sys
import os
import argparse

# Add the app directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app.data_processor import ThesisDataProcessor
from app.config import settings

def main():
    parser = argparse.ArgumentParser(description="Prepare thesis data for the chatbot")
    parser.add_argument(
        "pdf_path", 
        nargs='?', 
        default=None,
        help="Path to the thesis PDF file (default: data/raw/thesis.pdf)"
    )
    parser.add_argument(
        "--force", 
        action="store_true",
        help="Force reprocessing even if processed data already exists"
    )
    
    args = parser.parse_args()
    
    # Determine PDF path
    if args.pdf_path is None:
        pdf_path = os.path.join(settings.raw_data_path, "thesis.pdf")
    else:
        pdf_path = args.pdf_path
    
    # Check if PDF exists
    if not os.path.exists(pdf_path):
        print(f"Error: PDF file not found at {pdf_path}")
        print("Please either:")
        print("1. Place your thesis.pdf in the data/raw/ directory, or")
        print("2. Provide the path to your PDF as an argument")
        return 1
    
    try:
        # Initialize processor
        processor = ThesisDataProcessor()
        
        # Check if we should force reprocessing
        if args.force:
            print("Force reprocessing enabled...")
            # Remove existing processed data
            import shutil
            if os.path.exists(processor.chunks_file):
                os.remove(processor.chunks_file)
            if os.path.exists(processor.embeddings_file):
                os.remove(processor.embeddings_file)
        
        # Process the thesis
        print(f"Processing thesis from: {pdf_path}")
        chunks, embeddings = processor.process_thesis(pdf_path)
        
        print(f"\n✅ Data preparation complete!")
        print(f"📝 Created {len(chunks)} text chunks")
        print(f"🔢 Generated embeddings with shape: {embeddings.shape}")
        print(f"💾 Saved processed data to:")
        print(f"   - Chunks: {processor.chunks_file}")
        print(f"   - Embeddings: {processor.embeddings_file}")
        print(f"\nYou can now start the chatbot API with: python -m app.main")
        
        return 0
        
    except Exception as e:
        print(f"❌ Error during data preparation: {e}")
        return 1

if __name__ == "__main__":
    exit(main()) 