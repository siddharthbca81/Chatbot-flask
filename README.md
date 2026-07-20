# 🤖 Flask Chatbot

A simple web-based chatbot built using Python, Flask, HTML, CSS, and JavaScript. The chatbot uses rule-based keyword matching to generate responses in real-time without reloading the page.

## 👨‍💻 Created by
**Siddharth Pandey**

## 🛠️ Tech Stack
- **Python** – Core chatbot logic
- **Flask** – Backend web framework
- **HTML** – Page structure
- **CSS** – Styling and chat UI design
- **JavaScript** – Real-time interactivity using fetch API

## ⚙️ How It Works
1. User types a message in the chat interface
2. JavaScript sends the message to the Flask backend using `fetch()`
3. Python checks the message against predefined keywords
4. A matching reply is generated and sent back as JSON
5. JavaScript displays the reply instantly in the chat window

## 🚀 How to Run
1. Clone this repository
git clone https://github.com/siddharthbca81/Chatbot-flask.git

2. Navigate to the project folder

cd Chatbot-flask

3. Install Flask (if not already installed)

pip install flask

4. Run the app

python app.py

5. Open your browser and go to

http://127.0.0.1:5000

## ✨ Features
- Rule-based keyword matching
- Real-time chat without page reload
- JSON-based communication between frontend and backend
- Simple and clean chat UI

## 📌 Example Questions to Try
- "hi" / "hello"
- "how are you"
- "who created you"
- "what is python"
- "what is flask"
- "tell me a joke"

## 🔮 Future Improvements
- Integrate NLP/AI models for better context understanding
- Add more conversational topics
- Deploy live using Render/Railway for public access
