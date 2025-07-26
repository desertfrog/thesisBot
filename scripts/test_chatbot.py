#!/usr/bin/env python3
"""
Simple CLI tool to test the thesis chatbot.
This allows you to ask questions directly without running the API server.

Usage:
    python scripts/test_chatbot.py
"""

import sys
import os

# Add the app directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app.chatbot import ThesisChatbot

def main():
    print("🤖 Thesis Chatbot CLI")
    print("=" * 50)
    
    try:
        # Initialize chatbot
        print("Initializing chatbot...")
        chatbot = ThesisChatbot()
        chatbot.load_data()
        print("✅ Chatbot ready!\n")
        
    except FileNotFoundError:
        print("❌ Error: Processed data not found.")
        print("Please run 'python scripts/prepare_data.py' first to process your thesis.")
        return 1
    except ValueError as e:
        print(f"❌ Configuration error: {e}")
        print("Make sure you have set ANTHROPIC_API_KEY in your .env file.")
        return 1
    except Exception as e:
        print(f"❌ Error initializing chatbot: {e}")
        return 1
    
    print("Ask questions about your thesis. Type 'quit' or 'exit' to stop.")
    print("Type 'help' for available commands.\n")
    
    while True:
        try:
            question = input("🔍 Question: ").strip()
            
            if not question:
                continue
                
            if question.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
                
            if question.lower() == 'help':
                print_help()
                continue
            
            # Process the question
            print("🤔 Thinking...")
            result = chatbot.answer_question(question)
            
            print(f"\n💬 Answer:")
            print("-" * 40)
            print(result['answer'])
            print("-" * 40)
            print(f"📊 Used {result['num_chunks_used']} chunks from the thesis")
            if result['chunk_indices']:
                print(f"📝 Chunk indices: {result['chunk_indices']}")
            print()
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error processing question: {e}")
            print("Please try again.\n")

def print_help():
    print("\n📚 Available commands:")
    print("  help    - Show this help message")
    print("  quit    - Exit the chatbot")
    print("  exit    - Exit the chatbot")
    print("  q       - Exit the chatbot")
    print("\n💡 Tips:")
    print("  - Ask specific questions about your thesis content")
    print("  - Try questions like 'What is the main contribution?'")
    print("  - Or 'What methodology was used?'")
    print("  - The more specific your question, the better the answer")
    print()

if __name__ == "__main__":
    exit(main()) 