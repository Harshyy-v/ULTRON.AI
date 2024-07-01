import speech_recognition as sr
from langdetect import detect
from googletrans import Translator
import pyttsx3

id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\IVONA 2 Voice Brian22"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('rate', 180)
engine.setProperty('voice', id)


def speak(*args, **kwargs):
    audio = ""
    for i in args:
        audio += str(i)

    engine.say(audio)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening... (Say 'stop' to end)")
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


def translate_to_english(text):
    line = str(text)
    translator = Translator()
    translation = translator.translate(line)
    data = translation.text
    return data


def micexecution():
    query = listen()
    data = translate_to_english(query)
    print(f"YOU : {data}")
    return data
