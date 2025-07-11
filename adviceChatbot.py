import random

# Predefined responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm here to assist you!", "Feeling helpful today!"],
    "stress": ["Sometimes stress can feel overwhelming, but there are always ways to cope. Do you want to try some stress-relief techniques?"],
    "yes": ["Great! Let's start with some deep breathing exercises. Inhale deeply for 4 seconds, hold for 4 seconds, and exhale for 4 seconds. Do you feel better?", 
            "Okay! How about taking a short break, stretching, and going for a walk? Would you like to try that?"],
    "bye": ["Goodbye! Take care and remember to relax!", "See you later! Stay stress-free!"],
    "i'm stressed": ["I'm sorry to hear that! Would you like some tips for managing your stress?"],
    "i have a lot on my mind": ["It sounds like you're feeling overwhelmed. Would you like to try some relaxation techniques?"],
    "feeling overwhelmed": ["It can be hard to manage when everything piles up. Would you like some stress-relief suggestions?"],
    "default": ["I'm not sure I understand. Would you like stress-relief tips?", "Can you rephrase that? I’m here to help with stress."]
}

# Function to get a response
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

# Chat loop
print("Stress Advice Chatbot: Hi there! I'm here to help you manage stress. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Stress Advice Chatbot:", random.choice(responses["bye"]))
        break
    print("Stress Advice Chatbot:", get_response(user_input))
