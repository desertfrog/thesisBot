# Thesis Chatbot

**A demonstration project** showing how to build a conversational AI system for your thesis using Retrieval Augmented Generation (RAG). Ask questions about your thesis content and get intelligent responses powered by Voyage AI embeddings and Claude AI.

> 🎓 **Demo Purpose**: This project serves as an example implementation for creating thesis chatbots. Use it as a starting point to build your own!

## Features

- 📄 **PDF to Markdown**: Converts thesis PDF into searchable content  
- 🚀 **Voyage AI Embeddings**: High-quality semantic embeddings via API (no local models!)
- 🤖 **Claude AI Responses**: Natural language answers based on thesis content
- ⚡ **Fast Deployment**: Pre-computed embeddings for instant startup
- 🌐 **Web Interface**: Clean chat interface with table of contents

## Architecture 

- **Frontend**: GitHub Pages (static hosting)
- **Backend**: Render (FastAPI + pre-computed embeddings)  
- **Embeddings**: Voyage AI API (voyage-3.5-lite)
- **LLM**: Anthropic Claude (claude-3-5-haiku)

## Quick Setup

### 1. Get API Keys

You'll need:
- **Anthropic API Key**: [console.anthropic.com](https://console.anthropic.com/)
- **Voyage AI API Key**: [voyageai.com](https://voyageai.com)

### 2. Local Development

```bash
git clone <your-repo-url>
cd thesis_bot
pip install -r requirements.txt

# Configure environment
cp config/.env.example .env
# Edit .env with your API keys

# Add your thesis (optional - demo includes example)
cp your-thesis.pdf data/raw/thesis.pdf

# Generate embeddings (one-time)
python scripts/prepare_data.py

# Run locally  
python -m app.main
```

### 3. Deploy (Optional)

**Backend (Render)**:
- Connect your GitHub repo
- Add environment variables: `ANTHROPIC_API_KEY`, `VOYAGE_API_KEY`  
- Deploy automatically

**Frontend (GitHub Pages)**:
- Enable GitHub Pages in repo settings
- Update `API_BASE_URL` in `web-interface/script.js`

## Project Structure

```
thesis_bot/
├── app/                    # FastAPI backend
├── web-interface/          # Frontend (HTML/CSS/JS)
├── data/
│   ├── raw/thesis.md      # Your thesis content
│   ├── chunks/            # Pre-computed text chunks
│   └── embeddings/        # Pre-computed Voyage AI embeddings
├── notebooks/             # Jupyter notebook prototype
└── scripts/               # Utilities
```

## How It Works

1. **Text Processing**: Thesis → chunks → Voyage AI embeddings (1024-dim)
2. **Question Processing**: User question → Voyage AI embedding  
3. **Similarity Search**: Find most relevant thesis chunks
4. **Answer Generation**: Claude generates response based on relevant content

## Customization

**For Your Thesis**:
1. Replace `data/raw/thesis.md` with your content
2. Run `python scripts/prepare_data.py` to regenerate embeddings
3. Commit the new embeddings to your repo

**Model Options**:
- Embeddings: `voyage-3.5-lite`, `voyage-3.5`, `voyage-3-large`
- LLM: Any Claude model via Anthropic API

## Demo

- **Live Demo**: [Your GitHub Pages URL]
- **API Health**: [Your Render URL]/health

---

**Note**: This is a demonstration project. Adapt it for your specific thesis and requirements! 