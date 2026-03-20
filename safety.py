def check_crisis(text):
    text = text.lower()

    danger_phrases = [
        "i want to die",
        "kill myself",
        "end my life",
        "no reason to live"
    ]

    return any(phrase in text for phrase in danger_phrases)


def crisis_response():
    return (
        "I'm really sorry you're feeling this way. "
        "You don’t have to go through it alone. "
        "It might help to talk to someone you trust or a professional. "
        "Would you like me to stay here and talk with you?"
    )