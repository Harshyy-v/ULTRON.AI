import keyboard
import os

# Function to execute when hotkey is detected
def execute_hotkey():
    file_path = r'gui.py'
    os.system('python {}'.format(file_path))  # Execute the script

# Set up the hotkey (Windows key + 'j')
keyboard.add_hotkey('win+j', execute_hotkey)

# Keep the script running
keyboard.wait('esc')  # Wait until the 'esc' key is pressed to stop the script



