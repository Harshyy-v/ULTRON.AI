import pywhatkit
import speech_recognition as sr
import webbrowser
import wikipedia
from func.Speak import speak


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("ULTRON : What do you want to search sir ? ")
        speak("What do you want to search sir ?")
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


def searchGoogle():
    query = listen().lower()
    import wikipedia as wk
    query = query.replace("ultron", "")
    query = query.replace("google search", "")
    query = query.replace("google", "")
    speak("ULTRON :This is what I found on google .")
    try:
        pywhatkit.search(query)
        result = wk.summary(query, 1)
        speak(result)
    except:
        speak("ULTRON : No speakable output available")


def searchYoutube():
    query = listen().lower()
    speak("This is what I found for your search!")
    query = query.replace("youtube search", "")
    query = query.replace("youtube", "")
    web = "https://www.youtube.com/results?search_query=" + query
    webbrowser.open(web)
    pywhatkit.playonyt(query)
    speak("ULTRON :Done, Sir")


def searchWikipedia():
    query = listen().lower()
    speak("Searching from wikipedia....")
    query = query.replace("wikipedia", "")
    query = query.replace("search wikipedia", "")
    query = query.replace("tell me about", "")
    query = query.replace("who is", "")

    results = wikipedia.summary(query, sentences=1)
    speak("According to wikipedia..")
    print(f"ULTRON :{results}")
    speak(results)

