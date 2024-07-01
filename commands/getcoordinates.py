import pyautogui
import time

# Wait for a moment to give you time to position the mouse
print("Position your mouse where you want to get the coordinates...")
time.sleep(5)

# Get the current mouse position
current_pos = pyautogui.position()

# Print the coordinates
print("Mouse position:", current_pos)
