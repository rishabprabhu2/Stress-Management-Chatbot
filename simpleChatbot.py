import random

# Predefined responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm just a bot, but I'm doing great!", "I'm here to assist you!", "Feeling helpful today!"],
    "your name": ["I'm a simple chatbot.", "Call me ChatGPT Lite!", "I'm just a bot without a name."],
    "bye": ["Goodbye!", "See you later!", "Have a great day!"],
    "what can you do": ["I can chat with you and answer basic questions.", "I'm here to assist you with simple tasks!", "I can respond to various commands. Try asking 'how are you' or 'your name'."],
    "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!", "Why did the math book look sad? Because it had too many problems.", "Why can't your nose be 12 inches long? Because then it would be a foot!"],
    "what is the weather": ["I don't know the current weather, but it's always sunny in the chatbot world!", "I can't check the weather, but it's always a good time for a chat!"],
    "default": ["I'm not sure I understand.", "Can you rephrase that?", "Interesting! Tell me more."]
}

# Function to get a response
def get_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for case-insensitive matching
    
    # Check if any of the specific responses match
    for key in responses:
        if key in user_input:  # Check if the key is a substring of the user input
            return random.choice(responses[key])
    
    # Default response if no match found
    return random.choice(responses["default"])

# Chat loop
print("Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot:", random.choice(responses["bye"]))
        break
    print("Chatbot:", get_response(user_input))
