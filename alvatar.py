from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

# Create a new chatbot instance
chatbot = ChatBot(
    'InfoBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the English corpus
trainer.train('chatterbot.corpus.english')

# Train the chatbot with some custom data
trainer.train([
    "Hello, how can I help you?",
    "I am here to assist you with any questions you have about our services.",
    "What is your return policy?",
    "You can return any book within 30 days of purchase as long as it is in good condition.",
    "Do you offer international shipping?",
    "Yes, we do offer international shipping. Shipping costs vary depending on the destination.",
    "Can I track my order?",
    "Absolutely! Once your order is shipped, you'll receive a tracking number via email.",
    "What payment methods do you accept?",
    "We accept all major credit cards, PayPal, and bookstore gift cards."
])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['message']
    response = chatbot.get_response(user_input)
    return jsonify({'response': str(response)})

if __name__ == '__main__':
    app.run(debug=True)
