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

    # Negated emotions
    if any(phrase in text for phrase in ["not happy", "not great", "not feeling good", "never happy", "can't smile", "no joy"]):
        return "sad"
    if any(phrase in text for phrase in ["not sad", "not lonely", "not bored", "feel better", "not bad"]):
        return "happy"
    if any(phrase in text for phrase in ["not stressed", "relaxed", "calm down", "no worries"]):
        return "happy"

    # Direct keywords
    sad_words = ["sad", "lonely", "depressed", "tired", "down", "upset", "miserable", "crying", "heartbroken", "hopeless", "tear", "hurt", "empty"]
    happy_words = ["happy", "excited", "great", "awesome", "good", "glad", "joy", "amazing", "wonderful", "smiling", "love", "proud"]
    stressed_words = ["stressed", "anxious", "worried", "panic", "overwhelmed", "tense", "nervous", "pressure", "too much", "scared", "fear"]
    angry_words = ["angry", "mad", "furious", "annoyed", "frustrated", "hate", "irritating", "pissed", "rage"]
    bored_words = ["bored", "nothing to do", "uninterested", "dull", "yawn", "boring"]

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
        
    # Fallback to sentiment if we couldn't detect an explicit emotion word
    sentiment = detect_sentiment(text)
    if sentiment == "negative":
        # If no explicit negative emotion but the tone is negative, assume lightly stressed or sad
        return "sad"
    elif sentiment == "positive":
        return "happy"

    return "unknown"