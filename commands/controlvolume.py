import math
from comtypes import CLSCTX_ALL, cast
from ctypes import POINTER
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import speech_recognition as sr
from func.Speak import speak


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Tell me the desired volume you want :")
        speak("Tell me the desired volume you want :")
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


def get_valid_volume():
    while True:
        try:
            volume = int(listen())
            if 0 <= volume <= 100:
                return volume
            else:
                print("Please enter a value between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def volumeMain():
    # Get the desired volume from the user
    desired_volume = get_valid_volume()

    # Get the default audio device
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # Convert desired volume (0-100) to a volume level between 0.0 and 1.0
    # This represents the linear volume scale used by most audio systems
    new_volume = desired_volume / 100.0

    # Set the volume directly using the new_volume value
    volume.SetMasterVolumeLevelScalar(new_volume, None)

    print(f"Volume set to {desired_volume}%")
    speak(f"Volume set to {desired_volume}%")


