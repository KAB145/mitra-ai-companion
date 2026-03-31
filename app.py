from flask import Flask, render_template, request, jsonify

from emotion_detection import detect_sentiment, detect_emotion
from response_generator import generate_response
from memory import init_db, save_message, get_last_messages
from safety import check_crisis, crisis_response

app = Flask(__name__)

# Initialize DB
init_db()


def is_emotional(text):
    keywords = ["sad", "tired", "upset", "depressed", "not feeling well", "angry", "stressed"]
    return any(k in text.lower() for k in keywords)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").strip()

    if not user_input:
        return jsonify({"response": "I'm here whenever you're ready 😊"})

    #  Safety first
    if check_crisis(user_input):
        response = crisis_response()
        save_message(user_input, response)
        return jsonify({"response": response})

    #  Emotion detection
    sentiment = detect_sentiment(user_input)
    emotion = detect_emotion(user_input)

    #  Smart memory usage
    if is_emotional(user_input):
        memory = []
    else:
        memory = get_last_messages(limit=5, include_bot=True)

    #  Generate response
    response = generate_response(user_input, emotion, sentiment, memory)

    # 💾 Save
    save_message(user_input, response)

    return jsonify({
        "response": response,
        "emotion": emotion,
        "sentiment": sentiment
    })


if __name__ == "__main__":
    app.run(debug=True)

    #trigger
    