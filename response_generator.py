import random

def generate_response(sentiment, emotion, user_input, memory):

    user_input_lower = user_input.lower()

    
    if any(word in user_input_lower for word in ["hi", "hello", "hey", "greetings"]):
        return random.choice([
            "Hey there 😊 How are you feeling today?",
            "Hello! I'm really glad you came. What's on your mind?",
            "Hi! Ready to chat?"
        ])

    past_reference = ""
    
    if memory and random.random() < 0.4:
        if memory[-1].lower() not in user_input_lower:
            past_reference = f" earlier you mentioned '{memory[-1]}'."
    
   
    if emotion == "sad":
        responses = [
            "I'm really glad you reached out. Want to talk about what's been bothering you?",
            "That sounds heavy… I’m here with you. What’s on your mind?",
            "I'm so sorry you're feeling down. I'm here to listen."
        ]
        if past_reference:
            responses.append(f"I hear you. Since{past_reference} I keep thinking if that might be weighing on you?")
        return random.choice(responses)

    if emotion == "happy":
        responses = [
            "That’s awesome to hear! What made you feel this way?",
            "I love that energy 😊 Tell me more!",
            "I'm so glad things are going well for you right now."
        ]
        if past_reference:
            responses.append(f"I see you're feeling great! Do you think it's because{past_reference}")
        return random.choice(responses)

    if emotion == "stressed":
        responses = [
            "That sounds stressful. Want to break it down together?",
            "Take a deep breath… I’m here. What’s worrying you most?",
            "It's completely okay to feel overwhelmed."
        ]
        if past_reference:
            responses.append(f"Take a breath. Since{past_reference} let's take it one step at a time. What can I do to help?")
        return random.choice(responses)

    if emotion == "bored":
        responses = [
            "Let’s fix that 😄 What do you usually enjoy doing?",
            "Want me to suggest something fun?",
            "Boredom can be annoying! Let's talk about your hobbies."
        ]
        if past_reference:
            responses.append(f"Well, since{past_reference} maybe we can jump back to that topic to pass the time?")
        return random.choice(responses)

    if memory and random.random() < 0.3:
        if memory[-1].lower() not in user_input_lower:
            return f"Hmm, earlier you brought up '{memory[-1]}'. Can we talk more about that?"

    
    return random.choice([
        "I'm here with you. Tell me more.",
        "That sounds interesting. Can you explain a bit more?",
        "How has your day been aside from that?"
    ])