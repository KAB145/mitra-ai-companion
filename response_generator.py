import random


def generate_response(user_input, emotion, sentiment, memory):
    user_input_lower = user_input.lower()

    # ------------------ Greetings ------------------
    if any(w in user_input_lower for w in ["hi", "hello", "hey"]):
        return random.choice([
            "Hey! How are you feeling today?",
            "Hi there 😊 what's on your mind?",
            "Hello! I'm here for you—what's going on?"
        ])

    # ------------------ Farewell ------------------
    if any(w in user_input_lower for w in ["bye", "goodbye"]):
        return "Take care. I'm always here if you want to talk again 😊"

    # ------------------ Emotion-based ------------------

    if emotion == "sad":
        return random.choice([
            "I'm really sorry you're feeling this way. Want to talk about it?",
            "That sounds tough… I'm here to listen.",
            "Do you want to share what's been bothering you?"
        ])

    if emotion == "happy":
        return random.choice([
            "That's great to hear 😊 what made your day good?",
            "Love that! what's been going well?",
            "That sounds awesome—tell me more!"
        ])

    if emotion == "stressed":
        return random.choice([
            "Sounds like a lot is going on. Want to break it down together?",
            "That can feel overwhelming… what's the hardest part?",
            "Take it one step at a time—what's bothering you most?"
        ])

    if emotion == "angry":
        return random.choice([
            "That sounds frustrating… what happened?",
            "I get why you'd feel that way. Want to vent a bit?",
            "What triggered it the most?"
        ])

    # ------------------ Memory Awareness ------------------
    if memory:
        return "Earlier you mentioned something similar. Is this connected or something new?"

    # ------------------ Default ------------------
    return random.choice([
        "I'm listening—tell me more.",
        "What’s been on your mind about this?",
        "Can you explain a bit more?"
    ])