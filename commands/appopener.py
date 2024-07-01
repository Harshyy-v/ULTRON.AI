import AppOpener
import speech_recognition as sr
from func.Speak import speak


def listenforopen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("ULTRON : Which App do you want to open Sir ? ")
        speak("Which App do you want to open Sir ?")
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


def listentoclose():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("ULTRON : Which App do you want to close Sir ? ")
        speak("Which App do you want to close Sir ?")
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


def openapp():
    appname = listenforopen().lower()
    appname = appname.replace("kholo", "")
    appname = appname.replace("chalao", "")
    AppOpener.open(appname, match_closest=True)


def closeapp():
    appname = listentoclose().lower()
    appname = appname.replace("ko bandh karo" , "")
    appname = appname.replace("ko bandh kardo", "")

    AppOpener.close(appname, match_closest=True)

