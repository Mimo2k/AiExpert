import re
import random
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# Destination options with short descriptions
destinations = {
    "beaches": [("Bali", "a paradise of surf and sun"), 
                ("Maldives", "an island dream escape"), 
                ("Phuket", "Thailand’s tropical treasure")],
    "mountains": [("Swiss Alps", "snowy peaks and scenic trains"), 
                  ("Rocky Mountains", "adventure and wildlife"), 
                  ("Himalayas", "roof of the world")],
    "cities": [("Tokyo", "futuristic and full of culture"), 
               ("Paris", "the city of love"), 
               ("New York", "the city that never sleeps")]
}

# Jokes for TravelBot
jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!",
    "Why don’t mountains get tired? Because they always peak performance!",
    "I told my suitcase there’d be no vacation this year... now I’m dealing with emotional baggage."
]

# Normalize input
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

# Help menu
def show_help():
    print(Fore.MAGENTA + "\nTravelBot can:")
    print(Fore.GREEN + "- Suggest travel spots → say 'recommend' or 'suggest'")
    print(Fore.GREEN + "- Offer packing tips → say 'pack' or 'packing'")
    print(Fore.GREEN + "- Tell a joke → say 'joke' or 'funny'")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")

# Recommendation logic
def recommend():
    print(Fore.CYAN + "TravelBot: Do you prefer beaches, mountains, or cities?")
    while True:
        preference = normalize_input(input(Fore.YELLOW + "You: "))
        if preference in destinations:
            place, description = random.choice(destinations[preference])
            print(Fore.GREEN + f"TravelBot: How about {place}? It's {description}.")
            print(Fore.CYAN + "TravelBot: Do you like this suggestion? (yes/no)")
            answer = normalize_input(input(Fore.YELLOW + "You: "))
            if answer == "yes":
                print(Fore.GREEN + f"TravelBot: Awesome! Pack your bags for {place}! ✈️")
                break
            elif answer == "no":
                print(Fore.RED + "TravelBot: No problem! Let's try another option.")
            else:
                print(Fore.YELLOW + "TravelBot: I'll suggest again.")
        else:
            print(Fore.RED + "TravelBot: Hmm, I can only suggest from beaches, mountains, or cities.")

# Packing tip logic
def packing_tips():
    print(Fore.CYAN + "TravelBot: Where are you going?")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    
    while True:
        print(Fore.CYAN + "TravelBot: For how many days?")
        days = input(Fore.YELLOW + "You: ")
        if days.isdigit():
            days = int(days)
            break
        else:
            print(Fore.RED + "TravelBot: Please enter the number of days as a digit.")
    
    print(Fore.GREEN + f"\nTravelBot: Packing tips for {days} day{'s' if days != 1 else ''} in {location.title()}:")
    print("- Pack versatile clothes suitable for the climate.")
    if days > 5:
        print("- Bring extra clothes and laundry essentials.")
    else:
        print("- Keep it light! You won’t need too much.")
    print("- Don't forget your chargers and adapters.")
    print("- Always check the weather before packing!")

# Joke logic
def tell_joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)} 😂")

# Main chat loop
def chat():
    print(Fore.CYAN + "🌍 Hello! I'm TravelBot, your fun travel companion.")
    name = input(Fore.YELLOW + "TravelBot: What should I call you? ")
    name = name.strip().title() or "Traveler"
    print(Fore.GREEN + f"TravelBot: Nice to meet you, {name}! Let's explore the world 🌏")
    
    show_help()
    
    while True:
        user_input = normalize_input(input(Fore.YELLOW + f"{name}: "))
        
        if re.search(r"\brecommend\b|\bsuggest\b", user_input):
            recommend()
        elif re.search(r"\bpack\b|\bpacking\b", user_input):
            packing_tips()
        elif re.search(r"\bjoke\b|\bfunny\b", user_input):
            tell_joke()
        elif re.search(r"\bhelp\b", user_input):
            show_help()
        elif re.search(r"\b(exit|bye)\b", user_input):
            print(Fore.CYAN + "TravelBot: Safe travels! ✈️ Goodbye!")
            break
        else:
            print(Fore.RED + "TravelBot: Hmm... I didn’t get that. Type 'help' to see what I can do!")

# Run bot
if __name__ == "__main__":
    chat()
