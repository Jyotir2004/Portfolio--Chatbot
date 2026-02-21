"""
Response database for the portfolio chatbot.
Contains predefined responses organized by category.
"""

# Predefined responses organized by category
RESPONSES = {
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
KEYWORDS = {
    'greeting': ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon'],
    'name': ['name', 'who are you', 'what are you', 'introduce yourself', 'yourself'],
    'skills': ['skill', 'technology', 'programming', 'languages', 'technologies', 'abilities', 'expertise'],
    'education': ['education', 'degree', 'school', 'university', 'college', 'study', 'background'],
    'projects': ['project', 'work', 'portfolio', 'github', 'repository', 'applications', 'apps']
}

def get_response_by_category(category, index=None):
    """
    Get a response from a specific category.
    If index is provided, return the response at that index.
    Otherwise, return a random response from the category.
    """
    import random
    
    if category in RESPONSES:
        if index is not None and 0 <= index < len(RESPONSES[category]):
            return RESPONSES[category][index]
        else:
            return random.choice(RESPONSES[category])
    else:
        return random.choice(RESPONSES['default'])

def get_all_categories():
    """Return a list of all response categories."""
    return list(RESPONSES.keys())

def get_keywords_for_category(category):
    """Get keywords associated with a specific category."""
    return KEYWORDS.get(category, [])

def get_all_keywords():
    """Return a dictionary of all keywords."""
    return KEYWORDS
