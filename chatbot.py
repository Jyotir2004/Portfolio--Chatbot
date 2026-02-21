import re
import json
from datetime import datetime
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

try:
    # Download required NLTK data for sentiment analysis
    nltk.data.find('vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon')

class PortfolioChatbot:
    def __init__(self):
        self.chat_history = []
        self.sentiment_analyzer = SentimentIntensityAnalyzer()
        
        # Predefined responses organized by category
        self.responses = {
            'greeting': [
                "Hello! I'm your portfolio assistant. How can I help you today?",
                "Hi there! I'm here to answer questions about my portfolio. What would you like to know?",
                "Greetings! I'm your personal portfolio assistant. Feel free to ask me anything about my background!"
            ],
            'name': [
                "I'm a portfolio assistant chatbot designed to showcase a developer's skills and projects!",
                "My name is PortfolioBot. I'm here to help you learn more about the developer's background and work.",
                "I'm an AI assistant created to represent a developer's portfolio. You can ask me about their skills, education, and projects."
            ],
            'skills': [
                "The developer has expertise in Python, JavaScript, HTML, CSS, and various frameworks. They're skilled in web development, data analysis, and software engineering principles.",
                "Technical skills include proficiency in Python, JavaScript, React, Node.js, SQL, and cloud technologies. The developer also has experience with version control systems like Git.",
                "The developer is experienced in full-stack development, with strengths in backend technologies like Python/Django and frontend technologies like React and Vue.js."
            ],
            'education': [
                "The developer holds a Bachelor's degree in Computer Science from a reputable university. They also have several online certifications in specialized areas like machine learning and cloud computing.",
                "Educational background includes a Computer Science degree with coursework in algorithms, data structures, databases, and software engineering. Additional certifications in modern technologies.",
                "The developer graduated with a degree in Software Engineering and has continued learning through online courses and certifications in cutting-edge technologies."
            ],
            'projects': [
                "The developer has worked on several projects including a task management application, an e-commerce website, and a data visualization dashboard. Each project demonstrates different skills and technologies.",
                "Notable projects include a weather forecasting app using Python and APIs, a blog platform built with React and Node.js, and a machine learning model for predictive analytics.",
                "Projects showcase a variety of skills: a full-stack web application, a mobile-responsive website, and an automated data processing script. All projects are available on GitHub."
            ],
            'default': [
                "I'm not sure I understood that. Could you ask about my skills, education, or projects?",
                "I didn't quite catch that. You can ask me about the developer's background, skills, or projects.",
                "Sorry, I didn't understand. Try asking about skills, education, or projects.",
                "I'm here to help you learn about the developer's portfolio. What would you like to know about their skills, education, or projects?"
            ]
        }
        
        # Keywords to identify user intent
        self.keywords = {
            'greeting': ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon'],
            'name': ['name', 'who are you', 'what are you', 'introduce yourself', 'yourself'],
            'skills': ['skill', 'technology', 'programming', 'languages', 'technologies', 'abilities', 'expertise'],
            'education': ['education', 'degree', 'school', 'university', 'college', 'study', 'background'],
            'projects': ['project', 'work', 'portfolio', 'github', 'repository', 'applications', 'apps']
        }

    def preprocess_input(self, user_input):
        """Preprocess user input for better matching"""
        return user_input.lower().strip()

    def detect_intent(self, user_input):
        """Detect user intent based on keywords"""
        processed_input = self.preprocess_input(user_input)
        
        for intent, keywords in self.keywords.items():
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
        import random
        if intent in self.responses:
            response = random.choice(self.responses[intent])
        else:
            response = random.choice(self.responses['default'])
        
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

    def start_conversation(self):
        """Main conversation loop"""
        print("=" * 50)
        print("🤖 PORTFOLIO CHATBOT")
        print("=" * 50)
        
        # Initial greeting
        greeting = self.get_response("hello")
        print(f"\n🤖 {greeting}")
        
        while True:
            user_input = input("\n👤 You: ").strip()
            
            if not user_input:
                print("🤖 Please enter a message.")
                continue
            
            # Get response from chatbot
            response = self.get_response(user_input)
            
            # Add to chat history
            self.add_to_history(user_input, response)
            
            # Print bot response
            print(f"\n🤖 {response}")
            
            # Check if user wants to exit
            if self.detect_intent(user_input) == 'exit':
                break

    def save_chat_history(self, filename='chat_history.json'):
        """Save chat history to a file"""
        with open(filename, 'w') as f:
            json.dump(self.chat_history, f, indent=2)
        print(f"\n📝 Chat history saved to {filename}")

    def get_chat_summary(self):
        """Get a summary of the chat session"""
        if not self.chat_history:
            return "No chat history available."
        
        total_messages = len(self.chat_history)
        positive_interactions = sum(1 for entry in self.chat_history if entry['sentiment'] > 0.05)
        negative_interactions = sum(1 for entry in self.chat_history if entry['sentiment'] < -0.05)
        
        summary = f"""
📊 CHAT SUMMARY
{'-' * 20}
Total interactions: {total_messages}
Positive sentiments: {positive_interactions}
Negative sentiments: {negative_interactions}
Session ended at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        return summary


if __name__ == "__main__":
    # Create and start the chatbot
    bot = PortfolioChatbot()
    try:
        bot.start_conversation()
        print(bot.get_chat_summary())
        bot.save_chat_history()
    except KeyboardInterrupt:
        print("\n\n👋 Session ended by user. Goodbye!")
        print(bot.get_chat_summary())
        bot.save_chat_history()
