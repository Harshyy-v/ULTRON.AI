import os
import time
import datetime
import pyautogui
from func.Speak import speak


def take_screenshot():

    folder_path ="C:\\Users\\Harsham Vashisht\\OneDrive\\Pictures\\test"
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created folder: {folder_path}")

    # Generate a unique file name using the current timestamp
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"screenshot_{timestamp}.png"

    # Capture screenshot
    screenshot = pyautogui.screenshot()

    # Save the screenshot to the specified file path
    file_path = os.path.join(folder_path, file_name)
    screenshot.save(file_path)
    print(f"Screenshot saved to {file_path}")
    speak("Screenshot is saved.")


