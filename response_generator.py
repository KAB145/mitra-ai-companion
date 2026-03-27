import random
import re

def clean_memory_topic(text):
    # Try to extract the core topic from the user's previous message
    text = text.lower()
    # Remove common conversational fillers
    text = re.sub(r'^(i am|i feel|i think|i want to|i need to|i just)\s+', '', text)
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()

def generate_response(sentiment, emotion, user_input, memory):
    user_input_lower = user_input.lower()

    # Greetings
    if any(word in user_input_lower for word in ["hi", "hello", "hey", "greetings", "good morning", "good evening"]):
        return random.choice([
            "Hey! How are you doing today?",
            "Hi there! I'm glad you're here. What's on your mind?",
            "Hello! How has your day been treating you?",
            "Hey! Anything you'd like to chat about?"
        ])
        
    # Farewells
    if any(word in user_input_lower for word in ["bye", "goodbye", "see ya", "goodnight"]):
         return random.choice([
            "Take care! I'm always here if you need to talk again.",
            "Goodbye! Hope you have a wonderful rest of your day.",
            "See you later! Remember to take things one step at a time."
         ])

    # Smart memory referencing
    past_reference = ""
    if memory and random.random() < 0.35:  # 35% chance to bring up past context
        last_msg = memory[-1]
        topic = clean_memory_topic(last_msg)
        if topic and topic not in user_input_lower and len(topic) > 3:
            past_reference = topic
    
    # Emotion-based routing
    if emotion == "sad":
        responses = [
            "I hear you. That sounds really tough to deal with. Do you want to talk more about how you're feeling?",
            "I'm so sorry you're going through this. I'm here for you, whatever you need.",
            "It’s completely okay to feel down sometimes. Be gentle with yourself. What's weighing on you the most?",
            "That sounds heavy. I'm just listening—take all the time you need."
        ]
        if past_reference:
            responses.append(f"I'm sorry you're feeling down. I remember you mentioned '{past_reference}' earlier—is that still bothering you?")
            responses.append(f"That sounds hard. Between this and '{past_reference}', it seems like a lot to handle. How are you holding up?")
        return random.choice(responses)

    if emotion == "happy":
        responses = [
            "That's wonderful to hear! 😊 It’s always great when things look up.",
            "I love hearing that! What's the best part about it?",
            "That’s amazing! You deserve to feel good.",
            "You seem to be in a great mood! Tell me more about what's going on."
        ]
        if past_reference:
            responses.append(f"I'm so glad! Does this have anything to do with '{past_reference}' you brought up earlier?")
        return random.choice(responses)

    if emotion == "stressed":
        responses = [
            "Take a slow, deep breath. That sounds overwhelming, but we can just take it one step at a time.",
            "It sounds like you have a lot on your plate. What part of it feels the most stressful right now?",
            "I can totally see why that would make you anxious. Remember to give yourself a break.",
            "That sounds incredibly stressful. Let's talk through it. What's your immediate concern?"
        ]
        if past_reference:
            responses.append(f"It's completely normal to feel stressed, especially with '{past_reference}' on your mind too. Try to take a breather.")
        return random.choice(responses)

    if emotion == "angry":
        return random.choice([
            "I can tell you're upset, and your feelings are completely valid. Want to vent about it?",
            "That sounds incredibly frustrating. I'm here to listen if you want to let it all out.",
            "It's okay to be angry. What triggered this for you?"
        ])

    if emotion == "bored":
        responses = [
            "Sometimes boredom is just a sign you need a change of pace. What’s something you’ve always wanted to try?",
            "Let's shake things up! What's a topic you could talk about for hours?",
            "If you could be anywhere in the world doing anything right now, what would it be?"
        ]
        if past_reference:
            responses.append(f"Well, if you're bored, we could always go back to talking about '{past_reference}'? 😉")
        return random.choice(responses)

    # General / Unknown emotion
    general_responses = [
        "That's really interesting. Tell me more.",
        "I'm listening. How did that make you feel?",
        "I see. What do you think you're going to do next?",
        "Thanks for sharing that with me. What else is on your mind?"
    ]
    
    if past_reference and random.random() < 0.5:
        general_responses.append(f"Hmm, listening to you makes me think about when you said '{past_reference}' earlier. How does that connect?")
        
    return random.choice(general_responses)