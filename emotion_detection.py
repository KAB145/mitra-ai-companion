from textblob import TextBlob
from transformers import pipeline

# Load emotion model once
try:
    emotion_classifier = pipeline(
        "text-classification",
        model="j-hartmann/emotion-english-distilroberta-base",
        top_k=1
    )
except:
    emotion_classifier = None


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

    sad_words = ["sad", "lonely", "depressed", "down", "hopeless", "hurt", "empty"]
    happy_words = ["happy", "excited", "great", "good", "joy", "love"]
    stressed_words = ["stressed", "anxious", "worried", "overwhelmed", "pressure"]
    angry_words = ["angry", "mad", "frustrated", "annoyed"]
    bored_words = ["bored", "dull", "nothing to do"]

    if any(word in text for word in sad_words):
        return "sad"
    elif any(word in text for word in angry_words):
        return "angry"
    elif any(word in text for word in stressed_words):
        return "stressed"
    elif any(word in text for word in happy_words):
        return "happy"
    elif any(word in text for word in bored_words):
        return "bored"

    return "unknown"


def detect_emotion(text):
    """
    Main emotion detection function (use THIS in app.py instead of detect_emotion_keywords)
    """

    # 🧠 1. Try AI model
    if emotion_classifier:
        try:
            result = emotion_classifier(text)[0]
            label = result['label'].lower()

            # Normalize labels
            if label in ["sadness"]:
                return "sad"
            elif label in ["joy"]:
                return "happy"
            elif label in ["anger"]:
                return "angry"
            elif label in ["fear"]:
                return "stressed"
            elif label in ["surprise"]:
                return "surprised"

            return label
        except:
            pass  # fallback below

    # 🔁 2. Fallback to keyword detection
    keyword_emotion = detect_emotion_keywords(text)
    if keyword_emotion != "unknown":
        return keyword_emotion

    # 📊 3. Final fallback → sentiment
    sentiment = detect_sentiment(text)

    if sentiment == "negative":
        return "sad"
    elif sentiment == "positive":
        return "happy"

    return "neutral"