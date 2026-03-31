from textblob import TextBlob


def detect_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0.3:
        return "positive"
    elif polarity < -0.3:
        return "negative"
    return "neutral"


def detect_emotion(text):
    text = text.lower()

    if any(w in text for w in ["sad", "down", "depressed", "lonely"]):
        return "sad"

    if any(w in text for w in ["happy", "great", "good", "excited"]):
        return "happy"

    if any(w in text for w in ["stress", "anxious", "overwhelmed", "worried"]):
        return "stressed"

    if any(w in text for w in ["angry", "mad", "frustrated"]):
        return "angry"

    if any(w in text for w in ["bored", "nothing to do"]):
        return "bored"

    return "neutral"