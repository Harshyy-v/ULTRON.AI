import random
from func.Speak import speak
# List of jokes
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "What do you call a bear with no teeth? A gummy bear!",
    "Why don't skeletons fight each other? They don't have the guts!",
    "What do you call a boomerang that doesn't come back? A stick!",
    "Why don't oysters donate to charity? Because they're shellfish!",
    "What do you call a fish wearing a bowtie? Sofishticated!",
    "Why don't elephants use computers? They're afraid of the mouse!",
    "What do you call a fake noodle? An impasta!",
    "Why don't seagulls fly over the bay? Because then they'd be bagels!",
    "What do you call a sleepwalking nun? A roamin' Catholic!"
]


# Function to tell a random joke
def tell_joke():
    joke = random.choice(jokes)
    print(joke)
    speak(joke)


def JokeMain():
    tell_joke()
    print("Thanks for listening to the jokes! Goodbye!")



