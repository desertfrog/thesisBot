// Configuration - Render deployment URL
const API_BASE_URL = 'https://thesisbot.onrender.com';

class ThesisChatbot {
    constructor() {
        this.messageInput = document.getElementById('messageInput');
        this.sendButton = document.getElementById('sendButton');
        this.chatMessages = document.getElementById('chatMessages');
        this.loadingOverlay = document.getElementById('loadingOverlay');
        this.status = document.getElementById('status');
        
        this.initializeEventListeners();
        this.updateStatus('Ready to answer questions!');
    }
    
    initializeEventListeners() {
        // Send button click
        this.sendButton.addEventListener('click', () => this.sendMessage());
        
        // Enter key press
        this.messageInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this.sendMessage();
            }
        });
        
        // Auto-resize input and character limit
        this.messageInput.addEventListener('input', () => {
            this.updateCharacterCount();
        });
        
        // Table of contents item clicks
        document.querySelectorAll('.toc-item').forEach(item => {
            item.addEventListener('click', () => {
                const question = item.getAttribute('data-question');
                this.askQuestion(question);
            });
        });
        

    }
    
    askQuestion(question) {
        this.messageInput.value = question;
        this.sendMessage();
    }
    
    async sendMessage() {
        const message = this.messageInput.value.trim();
        
        if (!message) {
            this.updateStatus('Please enter a question...');
            return;
        }
        
        // Add user message to chat
        this.addMessage(message, 'user');
        
        // Clear input and disable while processing
        this.messageInput.value = '';
        this.setLoading(true);
        
        try {
            // Call the API
            const response = await this.callAPI(message);
            
            // Add bot response
            this.addMessage(response.answer, 'bot');
            this.updateStatus(`Used ${response.num_chunks_used} thesis sections to answer`);
            
        } catch (error) {
            console.error('Error calling API:', error);
            this.addMessage(
                "I'm sorry, I encountered an error while processing your question. " +
                "This might be because the server is starting up (takes ~30 seconds on first use) " +
                "or there's a connection issue. Please try again in a moment.",
                'bot',
                true
            );
            this.updateStatus('Error occurred - please try again');
        } finally {
            this.setLoading(false);
        }
    }
    
    async callAPI(question) {
        const response = await fetch(`${API_BASE_URL}/ask`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                question: question,
                use_threshold: false,
                similarity_threshold: 0.75
            })
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        return await response.json();
    }
    
    addMessage(content, sender, isError = false) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}-message`;
        
        const contentDiv = document.createElement('div');
        contentDiv.className = `message-content ${isError ? 'error-message' : ''}`;
        
        // Simple line break preservation for bot messages
        if (sender === 'bot' && !isError) {
            // Just convert line breaks to HTML breaks - keep it simple!
            contentDiv.innerHTML = content.replace(/\n/g, '<br>');
        } else {
            // For user messages and errors, use plain text
            contentDiv.textContent = content;
        }
        
        messageDiv.appendChild(contentDiv);
        this.chatMessages.appendChild(messageDiv);
        
        // Scroll to bottom
        this.chatMessages.scrollTop = this.chatMessages.scrollHeight;
    }
    
    setLoading(isLoading) {
        if (isLoading) {
            this.loadingOverlay.style.display = 'flex';
            this.sendButton.disabled = true;
            this.messageInput.disabled = true;
            this.updateStatus('Thinking...');
        } else {
            this.loadingOverlay.style.display = 'none';
            this.sendButton.disabled = false;
            this.messageInput.disabled = false;
            this.messageInput.focus();
        }
    }
    
    updateStatus(message) {
        this.status.textContent = message;
    }
    
    updateCharacterCount() {
        const remaining = 500 - this.messageInput.value.length;
        if (remaining < 50) {
            this.updateStatus(`${remaining} characters remaining`);
        } else {
            this.updateStatus('Ready to answer questions!');
        }
    }
}

// Initialize the chatbot when the page loads
document.addEventListener('DOMContentLoaded', () => {
    new ThesisChatbot();
}); 