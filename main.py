# -----------------------------------------------
# Project 2 – AI Study Buddy (Rule-Based Chat Assistant)
# Created by: Vaishnavi Gupta
# -----------------------------------------------

import datetime
import time

# --- Step 1: Time-based greeting ---
hour = datetime.datetime.now().hour
name=input("enter a name: ")
if 5 <= hour < 12:
    print("Good morning, name! ☀️")
elif 12 <= hour < 17:
    print("Good afternoon, name! 🌤️")
elif 17 <= hour < 21:
    print("Good evening, name! 🌇")
else:
    print("Good night, name! 🌙")

# -----------------------------------------------

print("\n🤖 Hello! I am Vaishnavi's Study Buddy!")
print("You can talk to me. Type 'bye' anytime to exit.\n")

# --- Step 2: Chatbot memory (dictionary of responses) ---

responses = {
    "greeting": {
        "keywords": ["hello", "hey", "hii", "hi"],
        "response": "Hi there! How can I help you today?"
    },

    "introduction": {
        "keywords": ["who are you", "your name", "introduce yourself"],
        "response": "I'm your friendly AI Study Buddy created by Vaishnavi!"
    },

    "wellbeing": {
        "keywords": ["how are you", "how do you feel"],
        "response": "I'm just code, but I feel great when you run me!"
    },

    "motivation": {
        "keywords": ["motivate me", "inspire me", "encourage me"],
        "response": "Keep going! Every bug you fix makes you a better coder! 💪"
    },

    "python": {
        "keywords": ["python", "coding", "programming"],
        "response": "Python is powerful — it can do AI, automation, and much more!"
    },

    "sad": {
        "keywords": ["sad", "upset", "unhappy"],
        "response": "Don't worry! Even code breaks sometimes, but it always runs again! 😊"
    },

    "happy": {
        "keywords": ["happy", "excited", "feeling good"],
        "response": "That's great to hear! Keep that positive energy going! 🎉"
    },

    "time": {
        "keywords": ["time", "current time", "what time is it"],
        "response": f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"
    },

    "farewell": {
        "keywords": ["bye", "goodbye", "see you"],
        "response": "Goodbye! Keep learning and keep smiling! 😊"
    }
}

# --- Step 3: Function to find matching response ---

def get_response(user_input):
    user_input = user_input.lower()

    for category in responses:
        keywords = responses[category]["keywords"]

        for word in keywords:
            if word in user_input:
                return responses[category]["response"]

    return "Hmm... I'm not sure about that yet, but I'll learn soon!"

# --- Step 4: Main chat loop ---

while True:
    user = input("Your Question: ")
    reply = get_response(user)
    time.sleep(0.7)  # slight delay for realistic feel
    print("Bot Answer:", reply)

    if any(word in user.lower() for word in ["bye", "goodbye", "see you"]):
    break