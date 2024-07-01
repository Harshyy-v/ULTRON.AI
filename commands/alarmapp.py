import time
import pyautogui
import speech_recognition as sr
from func.Speak import speak


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("UlTRON: Please speak the time for the alarm (in format HH:MM AM/PM)")
        print("Listening...")
        recognizer.pause_threshold = 1
        recognizer.energy_threshold = 300

        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source, 0, 5)

    print("Recognizing...")

    try:
        # Recognize speech
        spoken_time = recognizer.recognize_google(audio_data)

    except sr.RequestError as e:
        print(f"Error: {e}")
        return "", "", ""

    spoken_time = spoken_time.replace(".", "").strip()  # Remove dot and extra whitespace
    spoken_time_split = spoken_time.split(":")

    if len(spoken_time_split) != 2:
        print("Invalid time format. Please try again.")
        return "", "", ""

    hour, minute_ampm = spoken_time_split
    minute_ampm = minute_ampm.split()

    if len(minute_ampm) != 2:
        print("Invalid time format. Please try again.")
        return "", "", ""

    minute, am_pm = minute_ampm[0], minute_ampm[1].lower()  # Convert AM/PM to lowercase
    return hour, minute, am_pm


# Function to set the alarm in the Windows Clock app
def open_windows_clock_app():
    # Open the Start menu
    pyautogui.press('win')

    # Search for the Alarms & Clock app
    pyautogui.write('clock', interval=0.1)
    pyautogui.press('enter')
    time.sleep(2)  # Wait for the app to open


def set_windows_alarm(hour, minute, am_pm):
    # Open the Clock app if it's not already open
    if "Alarms & Clock" not in pyautogui.getActiveWindowTitle():
        open_windows_clock_app()

    # Click on the Alarm tab
    pyautogui.click(120, 171)  # Adjust the coordinates based on your screen resolution
    time.sleep(1)

    # Click on the Add an alarm button
    add_alarm_coordinates = [(1272, 941), (1271, 901)]
    button_clicked = False
    for coordinate in add_alarm_coordinates:
        pyautogui.click(coordinate)
        time.sleep(1)

    # Set the alarm time
    pyautogui.write(hour)
    pyautogui.press('tab')
    pyautogui.write(minute)
    pyautogui.press('tab')
    pyautogui.write(am_pm)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')


# Main funcction
def main():
    hour, minute, am_pm = listen()
    if hour and minute and am_pm:
        print("Alarm set for {}:{} {}".format(hour, minute, am_pm.upper()))
        set_windows_alarm(hour, minute, am_pm)
    else:
        print("No valid time detected. Please try again.")

