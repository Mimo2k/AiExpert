import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from colorama import init, Fore
import time
import sys

init(autoreset=True)

# Load dataset
def load_data(file_path='imdb_top_1000.csv'):
    try:
        df = pd.read_csv(file_path)
        df['combined_features'] = df['Genre'].fillna('') + ' ' + df['Overview'].fillna('')
        return df
    except FileNotFoundError:
        print(Fore.RED + f"\nError: '{file_path}' not found. Please check the file path.")
        sys.exit()

movies_df = load_data()

# TF-IDF & Cosine Similarity
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies_df['combined_features'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# List genres
def list_genres(df):
    genres = set()
    for items in df['Genre'].dropna():
        for genre in items.split(','):
            genres.add(genre.strip())
    return sorted(genres)

genres = list_genres(movies_df)

# Processing animation
def processing_animation(message="Processing"):
    print(Fore.BLUE + f"\n{message}", end="", flush=True)
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print()

# Recommend movies
def recommend_movies(genre=None, mood=None, rating=None, top_n=5):
    df = movies_df.copy()

    if genre:
        df = df[df['Genre'].str.contains(genre, case=False, na=False)]
    if rating:
        df = df[df['IMDB_Rating'] >= rating]

    df = df.sample(frac=1).reset_index(drop=True)

    recommendations = []
    for _, row in df.iterrows():
        overview = row['Overview']
        if pd.isna(overview): continue
        polarity = TextBlob(overview).sentiment.polarity

        if not mood or (
            (TextBlob(mood).sentiment.polarity >= 0 and polarity >= 0) or
            (TextBlob(mood).sentiment.polarity < 0 and polarity < 0)
        ):
            recommendations.append((row['Series_Title'], polarity))

        if len(recommendations) == top_n:
            break

    return recommendations if recommendations else "No suitable movie recommendations found."

# Display recommendations
def display_recommendations(recs, name):
    print(Fore.YELLOW + f"\n🎬 Recommended Movies for {name}:")
    for i, (title, polarity) in enumerate(recs, 1):
        sentiment = (
            "😊 Positive" if polarity > 0 else
            "😞 Negative" if polarity < 0 else
            "😐 Neutral"
        )
        print(f"{Fore.CYAN}{i}. {title} ({sentiment}, Polarity: {polarity:.2f})")

# Handle recommendation flow
def handle_ai(name):
    print(Fore.GREEN + "\nAvailable Genres:")
    for idx, genre in enumerate(genres, 1):
        print(f"{Fore.CYAN}{idx}. {genre}")
    
    # Choose genre
    while True:
        genre_input = input(Fore.YELLOW + "\nEnter genre number or name: ").strip()
        if genre_input.isdigit() and 1 <= int(genre_input) <= len(genres):
            genre = genres[int(genre_input)-1]
            break
        elif genre_input.title() in genres:
            genre = genre_input.title()
            break
        print(Fore.RED + "Invalid genre. Please try again.")

    # Enter mood
    mood = input(Fore.YELLOW + "\nHow are you feeling today? (Describe your mood): ").strip()
    processing_animation("Analyzing your mood")

    polarity = TextBlob(mood).sentiment.polarity
    mood_desc = "😊 Positive" if polarity > 0 else "😞 Negative" if polarity < 0 else "😐 Neutral"
    print(Fore.GREEN + f"Detected mood: {mood_desc} (Polarity: {polarity:.2f})")

    # Rating input
    while True:
        rating_input = input(Fore.YELLOW + "\nEnter minimum IMDB rating (7.6 - 9.3) or type 'skip': ").strip().lower()
        if rating_input == 'skip':
            rating = None
            break
        try:
            rating = float(rating_input)
            if 7.6 <= rating <= 9.3:
                break
            print(Fore.RED + "Rating must be between 7.6 and 9.3.")
        except ValueError:
            print(Fore.RED + "Invalid rating. Try again.")

    processing_animation(f"Finding movies for {name}")

    recs = recommend_movies(genre, mood, rating)
    if isinstance(recs, str):
        print(Fore.RED + recs)
    else:
        display_recommendations(recs, name)

    # Offer more recommendations
    while True:
        more = input(Fore.YELLOW + "\nWant more recommendations? (yes/no): ").strip().lower()
        if more == "no":
            print(Fore.GREEN + f"\nEnjoy your movie time, {name}! 🍿🎥")
            break
        elif more == "yes":
            processing_animation("Fetching more picks")
            recs = recommend_movies(genre, mood, rating)
            if isinstance(recs, str):
                print(Fore.RED + recs)
            else:
                display_recommendations(recs, name)
        else:
            print(Fore.RED + "Please type 'yes' or 'no'.")

# Main
def main():
    print(Fore.BLUE + "\n🎉 Welcome to AI Movie Buddy – Your Personalized Movie Recommender!\n")
    name = input(Fore.YELLOW + "What's your name? ").strip().title()
    print(Fore.GREEN + f"\nAwesome to meet you, {name}! Let's dive into movies you’ll love!")
    handle_ai(name)

if __name__ == "__main__":
    main()
