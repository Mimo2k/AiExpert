import random
import csv
from datetime import datetime
from colorama import Fore, Style, init
from textblob import TextBlob

# Initialize colorama
init()

# Emojis for introduction
print(f"{Fore.CYAN}👋🕵️ Welcome to Sentiment Spy! {Style.RESET_ALL}")

# Ask user name
user_name = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL} ").strip()
if not user_name:
    user_name = "Mystery Agent"

# Store conversation history
conversation_history = []

# Instructions
print(f"\n{Fore.GREEN}Hello, Agent {user_name}!")
print(f"Type a sentence and I will analyze the sentiment using TextBlob. 🧠")
print(f"{Fore.YELLOW}Commands:")
print(f" - 'history' to view conversation")
print(f" - 'reset' to clear history")
print(f" - 'exit' to quit{Style.RESET_ALL}\n")

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}")
        continue

    # Exit command
    if user_input.lower() == "exit":
        print(f"\n{Fore.BLUE}👋 Exiting Sentiment Spy. Farewell, Agent {user_name}! 🕵️{Style.RESET_ALL}")
        break

    # Reset command
    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.CYAN}🧹 All conversation history cleared!{Style.RESET_ALL}")
        continue

    # History command
    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}📜 Conversation History:{Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type, timestamp) in enumerate(conversation_history, start=1):
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = random.choice(["😊", "😄", "👍", "🎉"])
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = random.choice(["😞", "😢", "💔", "☹️"])
                else:
                    color = Fore.YELLOW
                    emoji = random.choice(["😐", "🤔", "🧐"])

                print(f"{idx}. {color}{emoji} {text} "
                      f"(Polarity: {polarity:.2f}, {sentiment_type}, at {timestamp}){Style.RESET_ALL}")
        continue

    # Analyze sentiment
    try:
        polarity = TextBlob(user_input).sentiment.polarity
    except Exception as e:
        print(f"{Fore.RED}⚠️ Could not analyze sentiment. Please try again.{Style.RESET_ALL}")
        continue

    # Determine sentiment type
    if polarity >= 0.5:
        sentiment_type = "Positive"
        sentiment_strength = "Strongly Positive"
        color = Fore.GREEN
        emoji = random.choice(["😊", "😄", "👍", "🎉"])
    elif polarity > 0.25:
        sentiment_type = "Positive"
        sentiment_strength = "Slightly Positive"
        color = Fore.GREEN
        emoji = random.choice(["😊", "😄", "👍", "🎉"])
    elif polarity <= -0.5:
        sentiment_type = "Negative"
        sentiment_strength = "Strongly Negative"
        color = Fore.RED
        emoji = random.choice(["😞", "😢", "💔", "☹️"])
    elif polarity < -0.25:
        sentiment_type = "Negative"
        sentiment_strength = "Slightly Negative"
        color = Fore.RED
        emoji = random.choice(["😞", "😢", "💔", "☹️"])
    else:
        sentiment_type = "Neutral"
        sentiment_strength = "Neutral"
        color = Fore.YELLOW
        emoji = random.choice(["😐", "🤔", "🧐"])

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save to history
    conversation_history.append((user_input, polarity, sentiment_type, timestamp))

    # Save to CSV (optional)
    with open("sentiment_log.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([user_name, user_input, polarity, sentiment_type, timestamp])

    # Output result
    print(f"{color}{emoji} {sentiment_type} sentiment detected! ({sentiment_strength}) "
          f"Polarity: {polarity:.2f}{Style.RESET_ALL}")
