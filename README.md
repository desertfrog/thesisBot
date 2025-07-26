# Thesis Chatbot

A conversational AI system that allows you to ask questions about your thesis using Retrieval Augmented Generation (RAG). This project processes your thesis PDF, creates semantic embeddings, and uses Claude (Anthropic) to provide intelligent answers based on the content.

## Features

- 📄 **PDF Processing**: Automatically converts your thesis PDF to searchable chunks
- 🔍 **Semantic Search**: Uses sentence transformers for intelligent content retrieval
- 🤖 **AI-Powered Answers**: Leverages Claude AI for natural language responses
- 🚀 **FastAPI Backend**: RESTful API ready for web integration
- 🔧 **Easy Setup**: Simple configuration for your own thesis

## Quick Start

### 1. Clone and Setup

```bash
git clone <your-repo-url>
cd thesis_bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
# Copy the example environment file
cp config/.env.example .env

# Edit .env and add your Anthropic API key
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

To get an Anthropic API key:
1. Visit [https://console.anthropic.com/](https://console.anthropic.com/)
2. Sign up/login and create an API key
3. Add it to your `.env` file

### 4. Add Your Thesis

Place your thesis PDF in the `data/raw/` directory and name it `thesis.pdf`, or use a custom path.

### 5. Process Your Thesis

```bash
# Process thesis.pdf from data/raw/
python scripts/prepare_data.py

# Or specify a custom path
python scripts/prepare_data.py /path/to/your/thesis.pdf
```

This step:
- Converts your PDF to markdown
- Splits it into semantic chunks
- Generates vector embeddings
- Saves processed data for fast loading

### 6. Start the API

```bash
python -m app.main
```

The API will be available at `http://localhost:8000`

### 7. Ask Questions

You can now interact with your thesis! Use the API endpoints:

```bash
# Ask a question
curl -X POST "http://localhost:8000/ask" \
     -H "Content-Type: application/json" \
     -d '{"question": "What is the main contribution of this thesis?"}'

# Check health
curl "http://localhost:8000/health"
```

Or visit `http://localhost:8000/docs` for the interactive API documentation.

## Project Structure

```
thesis_bot/
├── app/                    # Main application code
│   ├── __init__.py
│   ├── config.py          # Configuration and settings
│   ├── data_processor.py  # PDF processing and embeddings
│   ├── chatbot.py         # Core chatbot logic
│   └── main.py            # FastAPI application
├── data/                  # Data storage
│   ├── raw/              # Original thesis files
│   ├── processed/        # Processed text data
│   ├── chunks/           # Text chunks (pickle files)
│   └── embeddings/       # Vector embeddings (pickle files)
├── notebooks/            # Jupyter notebooks
│   └── thesisBotV0.ipynb # Original prototype
├── scripts/              # Utility scripts
│   └── prepare_data.py   # Data preparation script
├── config/               # Configuration files
│   └── .env.example      # Environment variables template
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## Configuration

Customize the behavior by editing your `.env` file:

```bash
# Required
ANTHROPIC_API_KEY=your_key_here

# Optional customizations
EMBEDDING_MODEL=all-MiniLM-L6-v2    # Sentence transformer model
CHUNK_SIZE=1000                      # Text chunk size
CHUNK_OVERLAP=100                    # Overlap between chunks
TOP_K_CHUNKS=3                       # Number of chunks to retrieve
MAX_TOKENS=1500                      # Max tokens in AI response
```

## API Endpoints

### POST `/ask`
Ask a question about your thesis.

**Request:**
```json
{
  "question": "What methodology was used?",
  "use_threshold": false,
  "similarity_threshold": 0.75
}
```

**Response:**
```json
{
  "answer": "The methodology used in this thesis...",
  "num_chunks_used": 3,
  "chunk_indices": [45, 67, 123],
  "question": "What methodology was used?"
}
```

### GET `/health`
Check if the chatbot is ready.

### POST `/process`
Reprocess the thesis data (useful if you update your PDF).

## Customization for Your Thesis

### Using Your Own PDF

1. Place your PDF in `data/raw/thesis.pdf`
2. Run `python scripts/prepare_data.py`
3. Start the API: `python -m app.main`

### Adjusting Retrieval

- **More context**: Increase `TOP_K_CHUNKS` or lower `similarity_threshold`
- **Less context**: Decrease `TOP_K_CHUNKS` or raise `similarity_threshold`
- **Different chunking**: Modify `CHUNK_SIZE` and `CHUNK_OVERLAP`

### Changing the AI Model

The system uses Claude 3.5 Haiku by default. To use a different model, edit `app/chatbot.py` and change the model name in the `generate_answer` method.

## Development

### Running in Development Mode

```bash
# Install development dependencies
pip install -r requirements.txt

# Run with auto-reload
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Adding New Features

The modular structure makes it easy to extend:

- **New retrieval methods**: Add to `app/chatbot.py`
- **Different AI providers**: Modify `app/chatbot.py`
- **New endpoints**: Add to `app/main.py`
- **Data processing**: Extend `app/data_processor.py`

## Deployment

### Environment Variables for Production

```bash
ANTHROPIC_API_KEY=your_production_key
```

### Docker Deployment (Optional)

Create a `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["python", "-m", "app.main"]
```

### Web Integration

The FastAPI backend is ready for frontend integration. Enable CORS for your domain in `app/main.py`:

```python
allow_origins=["https://yourdomain.com"]  # Replace "*" with your domain
```

## Troubleshooting

### Common Issues

1. **"ANTHROPIC_API_KEY not found"**
   - Make sure you created a `.env` file with your API key

2. **"Processed data not found"**
   - Run the data preparation script: `python scripts/prepare_data.py`

3. **PDF processing fails**
   - Ensure your PDF is readable and not password-protected
   - Try with a different PDF to test

4. **Memory issues**
   - Reduce `CHUNK_SIZE` or `TOP_K_CHUNKS` for large documents
   - Consider using a smaller embedding model

### Getting Help

1. Check the API documentation at `http://localhost:8000/docs`
2. Review the logs for detailed error messages
3. Ensure all dependencies are installed correctly

## Contributing

Feel free to submit issues and enhancement requests! This project is designed to be a template that others can easily adapt for their own theses.

## License

This project is open source. Please add an appropriate license based on your needs.

---

**Note**: This chatbot is designed to help you explore and understand your thesis content. Always verify important information and use the AI responses as a starting point for deeper investigation. 