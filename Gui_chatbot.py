"""
GUI interface for the portfolio chatbot using Tkinter.
Provides a graphical interface for interacting with the chatbot.
"""

import tkinter as tk
from tkinter import scrolledtext, END, DISABLED, NORMAL
from datetime import datetime
import json
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

try:
    # Download required NLTK data for sentiment analysis
    nltk.data.find('vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon')

from responses import RESPONSES, KEYWORDS, get_response_by_category


class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Portfolio Chatbot")
        self.root.geometry("700x600")
        self.root.configure(bg='#f0f0f0')
        
        # Initialize sentiment analyzer
        self.sentiment_analyzer = SentimentIntensityAnalyzer()
        
        # Chat history
        self.chat_history = []
        
        # Set up the GUI
        self.setup_gui()
        
        # Initial greeting
        self.display_message("🤖", get_response_by_category('greeting'))
        
    def setup_gui(self):
        """Set up the GUI components"""
        # Main frame
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Chat history display
        self.chat_display = scrolledtext.ScrolledText(
            main_frame, 
            wrap=tk.WORD, 
            state=DISABLED, 
            bg='white', 
            font=('Arial', 12),
            height=25
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Input frame
        input_frame = tk.Frame(main_frame, bg='#f0f0f0')
        input_frame.pack(fill=tk.X)
        
        # Entry widget for user input
        self.user_input = tk.Entry(
            input_frame, 
            font=('Arial', 12),
            bg='white',
            relief=tk.FLAT
        )
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=5, padx=(0, 10))
        self.user_input.bind('<Return>', self.send_message)
        
        # Send button
        send_button = tk.Button(
            input_frame,
            text="Send",
            command=self.send_message,
            bg='#4CAF50',
            fg='white',
            font=('Arial', 10, 'bold'),
            relief=tk.FLAT,
            padx=20
        )
        send_button.pack(side=tk.RIGHT)
        
        # Bind the Enter key to send message
        self.user_input.focus()
    
    def preprocess_input(self, user_input):
        """Preprocess user input for better matching"""
        return user_input.lower().strip()

    def detect_intent(self, user_input):
        """Detect user intent based on keywords"""
        processed_input = self.preprocess_input(user_input)
        
        for intent, keywords in KEYWORDS.items():
            for keyword in keywords:
                if keyword in processed_input:
                    return intent
        
        # Check for exit command
        if 'exit' in processed_input or 'quit' in processed_input or 'bye' in processed_input:
            return 'exit'
        
        return 'default'
    
    def get_response(self, user_input):
        """Generate response based on user input"""
        intent = self.detect_intent(user_input)
        
        if intent == 'exit':
            return "Thank you for chatting! Have a great day!"
        
        # Select a response randomly from the appropriate category
        if intent in RESPONSES:
            import random
            response = random.choice(RESPONSES[intent])
        else:
            import random
            response = random.choice(RESPONSES['default'])
        
        return response
    
    def analyze_sentiment(self, text):
        """Analyze sentiment of user input"""
        scores = self.sentiment_analyzer.polarity_scores(text)
        # Return compound score (-1 to 1, where > 0.05 is positive, < -0.05 is negative)
        return scores['compound']
    
    def add_to_history(self, user_input, bot_response):
        """Add conversation to history"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sentiment_score = self.analyze_sentiment(user_input)
        
        entry = {
            'timestamp': timestamp,
            'user_input': user_input,
            'bot_response': bot_response,
            'sentiment': sentiment_score
        }
        self.chat_history.append(entry)
    
    def display_message(self, sender, message):
        """Display a message in the chat window"""
        self.chat_display.config(state=NORMAL)
        self.chat_display.insert(END, f"{sender}: {message}\n\n")
        self.chat_display.config(state=DISABLED)
        self.chat_display.yview(END)  # Auto-scroll to the bottom
    
    def send_message(self, event=None):
        """Handle sending a message"""
        user_text = self.user_input.get().strip()
        
        if not user_text:
            return
        
        # Clear the input field
        self.user_input.delete(0, END)
        
        # Display user message
        self.display_message("👤 You", user_text)
        
        # Get response from chatbot
        response = self.get_response(user_text)
        
        # Add to chat history
        self.add_to_history(user_text, response)
        
        # Display bot response
        self.display_message("🤖 Bot", response)
        
        # Check if user wants to exit
        if self.detect_intent(user_text) == 'exit':
            self.root.after(2000, self.root.quit)  # Close the window after 2 seconds
    
    def save_chat_history(self, filename='gui_chat_history.json'):
        """Save chat history to a file"""
        with open(filename, 'w') as f:
            json.dump(self.chat_history, f, indent=2)


def main():
    """Main function to run the GUI chatbot"""
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()
    
    # Save chat history when closing
    app.save_chat_history()


if __name__ == "__main__":
    main()
