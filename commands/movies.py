import requests
import re
from func.Speak import speak
import speech_recognition as sr

# Define your TMDb API key
API_KEY = 'abfd61660bbd6bc946506bdb5ece8381'

# Base URL for TMDb API
BASE_URL = 'https://api.themoviedb.org/3'


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("How can I assist you today? (or type 'exit' to quit): ")
        speak("How can I assist you today?")
        recognizer.pause_threshold = 1
        recognizer.energy_threshold = 300

        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source, 0, 5)

        print("Recognizing...")

        try:
            # Recognize speech
            query = recognizer.recognize_google(audio_data)


        except sr.RequestError as e:
            print(f"Error: {e}")

        recognized_text = str(query).lower()

    return recognized_text


def get_genres():
    genres_url = f"{BASE_URL}/genre/movie/list"
    genres_params = {'api_key': API_KEY}
    genres_response = requests.get(genres_url, params=genres_params)
    genres = genres_response.json()['genres']
    return genres


def get_genre_id(genre_name):
    genres = get_genres()
    for genre in genres:
        if genre['name'].lower() == genre_name.lower():
            return genre['id']
    return None


def recommend_movies_by_genre(genre_id):
    recommendations_url = f"{BASE_URL}/discover/movie"
    recommendations_params = {
        'api_key': API_KEY,
        'with_genres': genre_id
    }
    recommendations_response = requests.get(recommendations_url, params=recommendations_params)
    recommendations = recommendations_response.json()['results']

    recommended_movies = []
    for movie in recommendations:
        recommended_movies.append({
            'title': movie['title'],
            'overview': movie['overview'],
            'release_date': movie['release_date'],
            'vote_average': movie['vote_average']
        })
    return recommended_movies


def get_movie_details(movie_title):
    search_url = f"{BASE_URL}/search/movie"
    search_params = {
        'api_key': API_KEY,
        'query': movie_title
    }
    search_response = requests.get(search_url, params=search_params)
    search_results = search_response.json()

    if search_results['total_results'] == 0:
        return f"No movies found with title '{movie_title}'."

    # Assume the first result is the most relevant
    movie_id = search_results['results'][0]['id']

    movie_details_url = f"{BASE_URL}/movie/{movie_id}"
    movie_details_params = {
        'api_key': API_KEY
    }
    movie_details_response = requests.get(movie_details_url, params=movie_details_params)
    movie_details = movie_details_response.json()

    return {
        'title': movie_details['title'],
        'overview': movie_details['overview'],
        'release_date': movie_details['release_date'],
        'vote_average': movie_details['vote_average']
    }


def extract_movie_title(input_str):
    # Regular expression to match common phrases indicating a movie request
    regex = r"(?:tell\s*me\s*about|details\s*about)\s*(.*)"
    match = re.search(regex, input_str, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return None


def liste(user_input):
    if 'recommend' in user_input or 'suggest' in user_input:
        genre_keywords = ['recommend', 'suggest', 'me', 'movie', 'movies', 'some', 'good']
        words = user_input.split()
        genre_name = ' '.join([word for word in words if word.lower() not in genre_keywords]).strip()

        if genre_name:
            genre_id = get_genre_id(genre_name)
            if genre_id:
                recommendations = recommend_movies_by_genre(genre_id)
                if recommendations:
                    speak("Here are some recommendations.")
                    print(f"\nRecommended {genre_name.capitalize()} Movies:")
                    for movie in recommendations:
                        print(f"Title: {movie['title']}")
                        print(f"Overview: {movie['overview']}")
                        print(f"Release Date: {movie['release_date']}")
                        print(f"Rating: {movie['vote_average']}")
                        print("-" * 40)
                else:
                    print(f"No recommendations found for the genre '{genre_name}'.")
            else:
                print(f"Genre '{genre_name}' not found.")
        else:
            print("Please specify the genre.")
            genre_input = input("Specify the genre: ").strip().lower()
            genre_id = get_genre_id(genre_input)
            if genre_id:
                recommendations = recommend_movies_by_genre(genre_id)
                if recommendations:
                    print(f"\nRecommended {genre_input.capitalize()} Movies:")
                    for movie in recommendations:
                        print(f"Title: {movie['title']}")
                        print(f"Overview: {movie['overview']}")
                        print(f"Release Date: {movie['release_date']}")
                        print(f"Rating: {movie['vote_average']}")
                        print("-" * 40)
                else:
                    print(f"No recommendations found for the genre '{genre_input}'.")
            else:
                print(f"Genre '{genre_input}' not found.")

    else:
        movie_title = extract_movie_title(user_input)
        if movie_title:
            movie_details = get_movie_details(movie_title)
            if isinstance(movie_details, str):
                print(movie_details)
            else:
                print(f"Title: {movie_details['title']}")
                print(f"Overview: {movie_details['overview']}")

                print(f"Release Date: {movie_details['release_date']}")
                print(f"Rating: {movie_details['vote_average']}")
                speak(movie_details['overview'])
        else:
            print("I'm sorry, I couldn't understand. Please try again.")


def Moviesmain():
    user_input = listen().strip().lower()
    if user_input == "exit":
        exit()

    liste(user_input)



