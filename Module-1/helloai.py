import time

# Greet the user
print("🤖 Hello! I am AI Bot. What's your name? 😊")
name = input("Your name: ")

# Respond to the user's name
print(f"Nice to meet you, {name}! 🌟")
time.sleep(1)

# Ask a question
print("How are you feeling today? (good/bad/other) 🧐")
mood = input("Your mood: ").strip().lower()

# Use conditional statements to respond based on input
if mood == "good":
    print("That's wonderful to hear! Keep smiling! 😄")
elif mood == "bad":
    print("Oh no 😔 I'm here if you want to chat. Hope your day gets brighter soon!")
else:
    print("Thanks for sharing. Emotions can be tricky sometimes, and that's okay. 💙")

time.sleep(1)
# End the conversation
print(f"It was lovely chatting with you, {name}. Take care and have a great day! 👋")
