import random
import re


def clean_memory_topic(text):
    text = text.lower()
    text = re.sub(r'^(i am|i feel|i think|i want to|i need to|i just)\s+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()


def generate_response(sentiment, emotion, user_input, memory):
    user_input_lower = user_input.lower()

    # -----------------------------
    # 1. Greetings
    # -----------------------------
    if any(word in user_input_lower for word in ["hi", "hello", "hey", "good morning", "good evening"]):
        return random.choice([
            "Hey, I’m really glad you’re here. How are you feeling today?",
            "Hi! What’s been on your mind lately?",
            "Hello! I’m here to listen—what’s going on?",
        ])

    # -----------------------------
    # 2. Farewell
    # -----------------------------
    if any(word in user_input_lower for word in ["bye", "goodbye", "goodnight"]):
        return random.choice([
            "Take care of yourself. I’ll be here whenever you want to talk again.",
            "Goodbye for now. Remember, you’re not alone in this.",
        ])

    # -----------------------------
    # 3. Memory reference
    # -----------------------------
    past_reference = None
    if memory and random.random() < 0.5:
        last_msg = memory[-1]
        topic = clean_memory_topic(last_msg)
        if topic and topic not in user_input_lower:
            past_reference = topic

    # -----------------------------
    # 4. Emotion-based responses (SMART)
    # -----------------------------

    # 😢 SAD
    if emotion == "sad":
        responses = [
            f"I’m really sorry you're feeling this way. When you said '{user_input}', it sounds heavy. Do you want to talk more about it?",
            f"That sounds really tough. What part of '{user_input}' is hurting you the most?",
            f"I hear you. '{user_input}' doesn’t sound easy to deal with. I’m here with you.",
        ]

        if past_reference:
            responses.append(
                f"You mentioned '{past_reference}' before, and now this… it seems like a lot has been building up. How are you holding up?"
            )

        return random.choice(responses)

    # 😊 HAPPY
    if emotion == "happy":
        responses = [
            f"That’s really nice to hear! 😊 What made you feel this way about '{user_input}'?",
            f"I love that energy! Tell me more about what’s going so well.",
            f"That’s awesome. Moments like this really matter—what’s the best part?",
        ]

        if past_reference:
            responses.append(
                f"That’s great! Is this connected to what you mentioned earlier about '{past_reference}'?"
            )

        return random.choice(responses)

    # 😰 STRESSED
    if emotion == "stressed":
        responses = [
            f"It sounds like a lot is going on. When you said '{user_input}', it feels overwhelming. Want to break it down together?",
            f"That really does sound stressful. What’s the most difficult part right now?",
            f"I can sense the pressure in what you said. Let’s take it one step at a time—what’s bothering you most?",
        ]

        if past_reference:
            responses.append(
                f"You’ve also been dealing with '{past_reference}'. No wonder it feels overwhelming. Which part is hardest?"
            )

        return random.choice(responses)

    # 😠 ANGRY
    if emotion == "angry":
        return random.choice([
            f"I can feel the frustration in '{user_input}'. What happened exactly?",
            f"That sounds really frustrating. Do you want to vent a bit more about it?",
            f"It makes sense you'd feel angry about that. What triggered it the most?",
        ])

    # 😐 BORED
    if emotion == "bored":
        responses = [
            "Sometimes boredom is a sign you need something new. What usually excites you?",
            "Let’s shake things up a bit—what’s something you haven’t tried in a while?",
        ]

        if past_reference:
            responses.append(
                f"We could go back to something you mentioned earlier like '{past_reference}'—maybe that still interests you?"
            )

        return random.choice(responses)

    # -----------------------------
    # 5. GENERAL (Fallback but SMART)
    # -----------------------------
    general_responses = [
        f"That’s interesting. When you said '{user_input}', what did you mean by that?",
        f"I’m listening. How did that situation make you feel exactly?",
        f"That sounds important. What do you think is the next step for you?",
        f"Thanks for sharing that. What’s been on your mind the most about it?",
    ]

    if past_reference:
        general_responses.append(
            f"This reminds me of when you mentioned '{past_reference}'. Do you think they’re connected?"
        )

    return random.choice(general_responses)