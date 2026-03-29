from flask import Flask, render_template, request, jsonify

from emotion_detection import detect_sentiment, detect_emotion
from response_generator import generate_response
from memory import init_db, save_message, get_last_messages
from safety import check_crisis, crisis_response

app = Flask(__name__)

# Initialize database
init_db()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").strip()

    # Handle empty input
    if not user_input:
        return jsonify({"response": "I'm here whenever you're ready to talk 😊"})

    #  Safety check (highest priority)
    if check_crisis(user_input):
        response = crisis_response()
        save_message(user_input, response)
        return jsonify({"response": response})

    #  Emotion + sentiment detection (UPGRADED)
    sentiment = detect_sentiment(user_input)
    emotion = detect_emotion(user_input)

    #  Get conversation memory
    memory = get_last_messages()

    #  Generate response
    response = generate_response(sentiment, emotion, user_input, memory)

    #  Save conversation
    save_message(user_input, response)

    return jsonify({
        "response": response,
        "emotion": emotion,       # optional (useful for frontend/mood tracking)
        "sentiment": sentiment    # optional
    })


if __name__ == "__main__":
    app.run(debug=True)