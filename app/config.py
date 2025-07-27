import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    anthropic_api_key: str = os.getenv("ANTHROPIC_API_KEY", "")
    voyage_api_key: str = os.getenv("VOYAGE_API_KEY", "")
    embedding_model: str = os.getenv("EMBEDDING_MODEL", "voyage-3.5-lite")
    chunk_size: int = int(os.getenv("CHUNK_SIZE", "1000"))
    chunk_overlap: int = int(os.getenv("CHUNK_OVERLAP", "100"))
    top_k_chunks: int = int(os.getenv("TOP_K_CHUNKS", "3"))
    max_tokens: int = int(os.getenv("MAX_TOKENS", "1500"))
    
    # Data paths
    raw_data_path: str = "data/raw"
    processed_data_path: str = "data/processed"
    embeddings_path: str = "data/embeddings"
    chunks_path: str = "data/chunks"
    
    class Config:
        env_file = ".env"

# Global settings instance
settings = Settings() 