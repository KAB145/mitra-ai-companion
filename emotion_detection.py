from textblob import TextBlob

def detect_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0.3:
        return "positive"
    elif polarity < -0.3:
        return "negative"
    else:
        return "neutral"


def detect_emotion_keywords(text):
    text = text.lower()

    
    if any(phrase in text for phrase in ["not happy", "not great", "not feeling good", "never happy"]):
        return "sad"
    if any(phrase in text for phrase in ["not sad", "not lonely", "not bored"]):
        return "happy"

    
    if any(word in text for word in ["sad", "lonely", "depressed", "tired", "down", "upset", "miserable"]):
        return "sad"
    elif any(word in text for word in ["happy", "excited", "great", "awesome", "good", "glad", "joy"]):
        return "happy"
    elif any(word in text for word in ["stressed", "anxious", "worried", "panic", "overwhelmed", "tense"]):
        return "stressed"
    elif any(word in text for word in ["bored", "nothing to do", "uninterested", "dull"]):
        return "bored"

    return "unknown"