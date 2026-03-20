# Mitra Chatbot 🤖💬

A simple chatbot web application designed to chat with users, detect their emotions using TextBlob, and respond accordingly using a basic keyword/sentiment-based response generator. It uses SQLite for memory storage of conversation history to make the chat feel slightly more contextual.

## 🚀 Features
- **Emotion Detection**: Uses TextBlob to detect positive/negative sentiment, plus basic keyword matching for emotions like happiness, sadness, stress, and boredom.
- **Contextual Memory**: Remembers recent past messages using SQLite to refer back to them during the chat.
- **Safety Check**: Basic static checking for crisis keywords to provide automated supportive responses.
- **Web Interface**: A Flask-based web frontend.

## Installation

1. Clone the repository or download the files.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows
   # source venv/bin/activate    # On macOS/Linux
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:
   ```bash
   python app.py
   ```
2. Open your browser and navigate to `http://127.0.0.1:5000/`.
3. Start chatting!

## Tech Stack
- **Backend**: Python, Flask, SQLite3
- **NLP**: TextBlob
- **Frontend**: HTML, CSS, JavaScript (in `templates` and `static`)
