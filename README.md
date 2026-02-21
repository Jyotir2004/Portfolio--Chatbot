# Portfolio Assistant Chatbot

A rule-based AI chatbot built with Python that simulates a personal portfolio assistant. The chatbot responds to predefined queries about a developer's background, skills, education, and projects using conditional logic and conversational flow.

## Features

- 🤖 **Greeting System**: Welcomes users when conversation starts
- 📚 **Information Queries**: Answers questions about skills, education, and projects
- 💬 **Continuous Conversation**: Maintains dialogue until user types "exit"
- 🎨 **Multiple Interfaces**: Command-line, Tkinter GUI, and Streamlit web interface
- 📊 **Chat History**: Stores conversation logs with timestamps
- 😊 **Sentiment Analysis**: Detects sentiment in user inputs
- 📝 **Clean Output**: Well-formatted responses for readability

## Installation

1. Clone or download this repository to your local machine
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Command-Line Version

Run the main chatbot from the terminal:

```bash
python chatbot.py
```

### Tkinter GUI Version

Launch the graphical interface:

```bash
python gui_chatbot.py
```

### Streamlit Web App

Start the web-based chatbot:

```bash
streamlit run streamlit_chatbot.py
```

## How It Works

The chatbot uses rule-based logic to match user inputs against predefined keywords:

- **Greetings**: "hello", "hi", "hey", etc.
- **Name inquiries**: "who are you", "introduce yourself", etc.
- **Skills**: "skills", "technologies", "programming", etc.
- **Education**: "education", "degree", "school", etc.
- **Projects**: "projects", "work", "portfolio", etc.

Responses are randomly selected from predefined categories to provide varied answers.

## File Structure

```
chatbot/
├── chatbot.py              # Main command-line chatbot logic
├── responses.py            # Response database and utilities
├── gui_chatbot.py          # Tkinter GUI interface
├── streamlit_chatbot.py    # Streamlit web interface
├── requirements.txt        # Dependencies
└── README.md               # Documentation
```

## Customization

You can easily customize the chatbot by modifying:

1. **responses.py**: Change the responses in the RESPONSES dictionary
2. **Keywords**: Update the KEYWORDS dictionary to recognize different phrases
3. **Categories**: Add new response categories and keywords

## Example Interactions

- "Hello" → Bot greets you
- "Tell me about your skills" → Bot describes technical skills
- "What projects have you worked on?" → Bot lists projects
- "What's your education?" → Bot shares educational background
- "exit" → Ends the conversation

## Technologies Used

- Python 3.x
- NLTK (Natural Language Toolkit) for sentiment analysis
- Tkinter for desktop GUI
- Streamlit for web interface
