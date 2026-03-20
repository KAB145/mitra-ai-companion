from flask import Flask, render_template, request, jsonify

from emotion_detection import detect_sentiment, detect_emotion_keywords
from response_generator import generate_response
from memory import init_db, save_message, get_last_messages
from safety import check_crisis, crisis_response

app = Flask(__name__)

init_db()

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    
    if check_crisis(user_input):
        response = crisis_response()
        save_message(user_input, response)
        return jsonify({"response": response})

    sentiment = detect_sentiment(user_input)
    emotion = detect_emotion_keywords(user_input)
    memory = get_last_messages()

    response = generate_response(sentiment, emotion, user_input, memory)

    save_message(user_input, response)

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)