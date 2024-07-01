import speech_recognition as sr
import pyautogui
import time
import os
from func.Speak import speak


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
            query = ""

        recognized_text = str(query).lower()

    return recognized_text


def write_to_notepad():
    # Open Notepad
    os.system("start notepad")
    time.sleep(2)  # Wait for Notepad to open

    print("ULTRON : You can start speaking. Say 'save' to stop writing and save.")
    speak("You can start speaking. Say 'save' to stop writing and save.")

    while True:
        user_input = listen().lower()
        if "save" in user_input:
            # Generate file name with timestamp
            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"speech_to_text_{timestamp}.txt"

            # Save the file
            pyautogui.hotkey("ctrl", "s")
            time.sleep(2)  # Wait for the Save dialog to open
            pyautogui.write(file_name)  # File name
            pyautogui.press("enter")
            print(f"Text saved to {file_name}")
            break  # Exit the loop if user says "save"
        else:
            # Type the spoken text into Notepad
            pyautogui.write(user_input + "\n")



