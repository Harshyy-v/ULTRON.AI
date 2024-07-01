import screen_brightness_control as sbc
from func.Speak import listen
import speech_recognition as sr
from func.Speak import speak


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Tell me desired brightness you want :")
        speak("Tell me desired brightness you want :")
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


def get_valid_brightness():
    """
    This function prompts the user for a brightness value (0-100),
    ensures it's within the valid range, and returns the integer value.
    """
    while True:
        try:
            brightness = int(listen())
            if 0 <= brightness <= 100:
                return brightness
            else:
                print("Please enter a value between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def BrightnessMain():
    # Get the desired brightness from the user
    desired_brightness = get_valid_brightness()

    # Set the brightness using screen_brightness_control
    sbc.set_brightness(desired_brightness)

    print(f"Brightness set to {desired_brightness}%")
    speak(f"Brightness set to {desired_brightness}%")


