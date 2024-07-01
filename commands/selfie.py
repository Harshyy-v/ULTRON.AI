import cv2
import os
import time
from func.Speak import speak


def take_selfie():

    folder_path = "C:\\Users\\Harsham Vashisht\\OneDrive\\Pictures\\test"
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Open default camera
    cap = cv2.VideoCapture(0)

    # Generate unique file name using timestamp
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"selfie_{timestamp}.jpg"

    speak("say cheese!!!")
    # Countdown before taking the selfie
    countdown = 4
    while countdown > 0:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Display the countdown on the frame
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, str(countdown), (250, 250), font, 7, (0, 0, 255), 10, cv2.LINE_AA)
        cv2.imshow('Selfie Camera', frame)

        # Wait for 1 second
        cv2.waitKey(1000)
        countdown -= 1

    # Capture the frame after countdown
    ret, frame = cap.read()
    if ret:
        # Display the resulting frame
        cv2.imshow('Selfie Camera', frame)

        # Save captured image
        file_path = os.path.join(folder_path, file_name)
        cv2.imwrite(file_path, frame)
        print("Selfie captured!")
        speak("Selfie captured!")
        cv2.waitKey(2000)  # Display the captured image for 2 seconds
    else:
        print("Failed to capture image")

    # Release the capture
    cap.release()
    cv2.destroyAllWindows()


# Example usage:

