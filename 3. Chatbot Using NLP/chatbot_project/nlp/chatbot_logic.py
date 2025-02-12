import random

# Sample chatbot responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I assist you?", "Greetings!"],
    "yo": ["Hi there!", "Hello!", "Hey! How can I assist you?", "Greetings!"],
    "how are you": [
        "I'm just a bot, but I'm doing great!", 
        "I'm fine! How about you?", 
        "Doing well! Thanks for asking.",
        "Feeling fantastic! What about you?"
    ],
    "what is your name": [
        "I'm your friendly chatbot!", 
        "I go by many names, but you can call me ChatBot.",
        "Just a humble bot here to assist you!"
    ],
    "who created you": [
        "I was created by an amazing developer!", 
        "A team of skilled coders brought me to life!",
        "My creators prefer to stay mysterious!"
    ],
    "tell me a joke": [
        "Why don't scientists trust atoms? Because they make up everything!",
        "I told my wife she should embrace her mistakes. She gave me a hug.",
        "Parallel lines have so much in common. It’s a shame they’ll never meet."
    ],
    "bye": ["Goodbye!", "See you later!", "Have a great day!", "Take care!"],
    "thank you": ["You're welcome!", "Glad to help!", "Anytime!", "No problem!"],
    "what can you do": [
        "I can chat with you, tell jokes, and provide basic information!",
        "I can answer questions, entertain you, and help with simple tasks.",
        "Try asking me something interesting!"
    ],
    "weather": [
        "I'm not a weather bot, but you can check online for accurate updates.",
        "I wish I could predict the weather, but I recommend checking a forecast site!",
        "I can guess... it's either sunny, rainy, or somewhere in between!"
    ],
    "default": [
        "I'm not sure how to respond to that.", 
        "Can you rephrase?", 
        "That's interesting! Tell me more.", 
        "Hmm... I'm still learning. Try asking something else!"
    ]
}


def get_chatbot_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])
