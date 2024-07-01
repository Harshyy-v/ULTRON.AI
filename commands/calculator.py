import os
import time
import pyautogui
import speech_recognition as sr
from func.Speak import speak
import pytesseract
import AppOpener


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


def close_calculator():
    os.system("taskkill /f /im Calculator.exe")
    os.system("taskkill /f /im ApplicationFrameHost.exe")


def calculate():
    # Open Calculator
    os.system("start calc")
    time.sleep(2)  # Wait for Calculator to open

    print("ULTRON : You can start speaking. Say 'close' to exit the calculator.")
    speak("You can start speaking. Say 'close' to exit the calculator.")

    while True:
        user_input = listen().lower()
        if "close" in user_input:
            print("Closing the calculator...")
            close_calculator()

            break  # Exit the loop if user says "close"
        elif "clean" in user_input:
            pyautogui.press("esc")  # Clear the screen
        else:
            # Type the spoken text into Calculator
            pyautogui.write(user_input)

            # Press the equals key to calculate
            pyautogui.press("enter")

            # Wait for a short moment to allow the result to appear
            time.sleep(0.5)



