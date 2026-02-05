# Simple content-based recommendation system

items = {
    "Action": ["Avengers", "John Wick", "Mad Max"],
    "Comedy": ["The Mask", "Jumanji", "Mr. Bean"],
    "Drama": ["Forrest Gump", "Titanic", "The Pursuit of Happyness"],
    "Sci-Fi": ["Interstellar", "Inception", "The Matrix"]
}

print(" Movie Recommendation System")
print("Available genres:")
for genre in items:
    print("-", genre)

user_choice = input("\nEnter your favorite genre: ").title()

if user_choice in items:
    print("\nRecommended movies for you:")
    for movie in items[user_choice]:
        print("•", movie)
else:
    print("\nSorry, genre not found. Please try again.")
