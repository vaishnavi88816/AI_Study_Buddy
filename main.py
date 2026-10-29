# -----------------------------------------------
# Project 2 – AI Study Buddy (Rule-Based Chat Assistant)
# Created by: Saumya Singh
# -----------------------------------------------

import datetime
import time

# --- Step 1: Time-based greeting ---
hour = datetime.datetime.now().hour

if 5 <= hour < 12:
    print("Good morning, Saumya! ☀️")
elif 12 <= hour < 17:
    print("Good afternoon, Saumya! 🌤️")
elif 17 <= hour < 21:
    print("Good evening, Saumya! 🌇")
else:
    print("Good night, Saumya! 🌙")

# -----------------------------------------------

print("\n🤖 Hello! I am Saumya's Study Buddy!")
print("You can talk to me. Type 'bye' anytime to exit.\n")

# --- Step 2: Chatbot memory (dictionary of responses) ---

responses = {
    "hello": "Hi there! How can I help you today?",
    "who are you": "I'm your friendly AI Study Buddy created by Saumya Singh.",
    "how are you": "I'm just code, but I feel great when you run me!",
    "motivate me": "Keep going! Every bug you fix makes you a better coder 💪",
    "python": "Python is powerful — it can do AI, automation, and much more!",
    "sad": "Don't worry! Even code breaks sometimes, but it always runs again 😊",
    "happy": "That's great to hear! Keep that positive energy going 🎉",
    "time": f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}",
    "bye": "Goodbye! Keep learning and keep smiling 😊"
}

# --- Step 3: Function to find matching response ---

def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return responses[key]
    return "Hmm... I'm not sure about that yet, but I'll learn soon!"

# --- Step 4: Main chat loop ---

while True:
    user = input("Your Question: ")
    reply = get_response(user)
    time.sleep(0.7)  # slight delay for realistic feel
    print("Bot Answer:", reply)

    if "bye" in user.lower():
        break