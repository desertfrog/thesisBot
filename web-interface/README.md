# Thesis Chatbot Web Interface

A clean, modern chat interface for interacting with the thesis chatbot API.

## Quick Setup

1. **Enable GitHub Pages**: Settings → Pages → Deploy from main branch
2. **Deploy API to Render**: Your FastAPI backend
3. **Update API URL** in `script.js`:
   ```javascript
   const API_BASE_URL = 'https://your-app-name.onrender.com';
   ```
4. **Add to Google Sites**: Link to `https://yourusername.github.io/thesis_bot/web-interface/`

## Files

- `index.html` - Chat interface
- `style.css` - Styling  
- `script.js` - API integration
- `README.md` - This file

## Local Testing

```bash
python -m app.main  # Start API server
open index.html     # View interface
``` 