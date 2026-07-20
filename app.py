from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def get_bot_response(user_input):
    user_input = user_input.lower()

    # --- Specific phrases first ---
    if "how are you" in user_input:
        return "I'm doing great, thanks for asking!"
    elif "who created you" in user_input or "who made you" in user_input:
        return "I was created by Siddharth Pandey, a developer learning Python and Flask!"
    elif "what can you do" in user_input:
        return "I can chat about greetings, jokes, my name, and a few fun topics!"
    elif "favourite color" in user_input or "favorite color" in user_input:
        return "I like blue — reminds me of clear skies!"
    elif "favourite food" in user_input or "favorite food" in user_input:
        return "I don't eat, but if I could, I'd try pizza!"
    elif "tell me a joke" in user_input or "joke" in user_input:
        return "Why don't programmers like nature? Too many bugs!"
    elif "what is python" in user_input:
        return "Python is a popular programming language known for being simple and readable!"
    elif "what is flask" in user_input:
        return "Flask is a lightweight Python framework used to build web applications!"
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're most welcome! Happy to help."
    elif "good morning" in user_input:
        return "Good morning! Hope you have a great day ahead!"
    elif "good night" in user_input:
        return "Good night! Sleep well and take care."
    elif "who are you" in user_input:
        return "I'm a simple rule-based chatbot built using Python and Flask!"

    # --- General single keywords last ---
    elif "hi" in user_input or "hello" in user_input:
        return "Hello! How are you?"
    elif "bye" in user_input:
        return "Goodbye! See you soon."
    elif "name" in user_input:
        return "I'm your friendly chatbot!"
    elif "age" in user_input:
        return "I'm timeless — I don't age like humans!"
    elif "weather" in user_input:
        return "I can't check live weather yet, but I hope it's nice outside!"
    elif "help" in user_input:
        return "I can chat about greetings, jokes, Python, Flask, and more. Try asking!"
    elif "love" in user_input:
        return "Aww, that's sweet! I appreciate you too."
    elif "sad" in user_input:
        return "I'm sorry to hear that. I hope things get better soon!"
    elif "happy" in user_input:
        return "That's wonderful to hear! Keep smiling!"
    else:
        return "Sorry, I don't understand that."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json["message"]
    bot_reply = get_bot_response(user_message)
    return jsonify({"response": bot_reply})


if __name__ == "__main__":
    app.run(debug=True)