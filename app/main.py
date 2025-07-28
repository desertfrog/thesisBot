"""
FastAPI application for the thesis chatbot.
"""

import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from .chatbot import ThesisChatbot
from .data_processor import ThesisDataProcessor

app = FastAPI(
    title="Thesis Chatbot API",
    description="A chatbot that answers questions about your thesis using RAG (Retrieval Augmented Generation)",
    version="1.0.0"
)

# Enable CORS for web frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global chatbot instance
chatbot = None

class QuestionRequest(BaseModel):
    question: str
    use_threshold: bool = False
    similarity_threshold: float = 0.75
    context_percentage: float = 5.0  # Percentage of total thesis to use as context

class QuestionResponse(BaseModel):
    answer: str
    num_chunks_used: int
    chunk_indices: list
    question: str

@app.on_event("startup")
async def startup_event():
    """Initialize the chatbot on startup."""
    global chatbot
    try:
        # Initialize chatbot - embeddings should already exist
        chatbot = ThesisChatbot()
        chatbot.load_data()
        print("Chatbot initialized successfully!")
    except Exception as e:
        print(f"Failed to initialize chatbot: {e}")
        print("Make sure pre-computed embeddings exist in data/embeddings/ and data/chunks/")
        raise e

@app.get("/")
async def root():
    """Root endpoint with basic information."""
    return {
        "message": "Thesis Chatbot API",
        "description": "Ask questions about the thesis",
        "endpoints": {
            "ask": "/ask",
            "health": "/health",
            "process": "/process"
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    if chatbot is None:
        raise HTTPException(status_code=503, detail="Chatbot not initialized")
    
    return {
        "status": "healthy",
        "chatbot_loaded": chatbot.chunks is not None and chatbot.embeddings is not None
    }

@app.post("/ask", response_model=QuestionResponse)
async def ask_question(request: QuestionRequest):
    """Ask a question about the thesis."""
    if not chatbot:
        raise HTTPException(status_code=503, detail="Chatbot not initialized")
    
    try:
        # Calculate number of chunks based on percentage (minimum 5%, total 365 chunks)
        total_chunks = 365
        min_percentage = 5.0
        percentage = max(request.context_percentage, min_percentage)
        top_k_chunks = max(1, int(total_chunks * percentage / 100))
        
        result = chatbot.answer_question(
            request.question,
            request.use_threshold,
            request.similarity_threshold,
            top_k=top_k_chunks
        )
        
        return QuestionResponse(
            question=request.question,
            answer=result["answer"],
            num_chunks_used=result["num_chunks_used"],
            chunk_indices=result["chunk_indices"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/process")
async def process_thesis():
    """
    Process the thesis PDF (run data preparation).
    This endpoint allows reprocessing if needed.
    """
    try:
        processor = ThesisDataProcessor()
        chunks, embeddings = processor.process_thesis()
        
        return {
            "message": "Thesis processed successfully",
            "num_chunks": len(chunks),
            "embeddings_shape": list(embeddings.shape)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing thesis: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port) 