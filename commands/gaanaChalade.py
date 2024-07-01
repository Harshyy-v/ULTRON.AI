import random
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import time


def gaane():
    pygame.mixer.init()

    # Set the directory path where the songs are located
    music_dir = "D:\\New folder\\Songs"

    # Get a list of all the song files in the directory
    songs = [file for file in os.listdir(music_dir) if file.endswith(".mp3")]

    # Check if there are any songs in the directory
    if not songs:
        print("No songs found in the directory.")
        exit()

    # Select a random song from the list
    selected_song = random.choice(songs)
    song_path = os.path.join(music_dir, selected_song)

    # Load and play the selected song
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

    print(f"Now playing: {selected_song}")

    # Generate a random play duration between 10 to 20 seconds
    play_duration = random.randint(10, 20)

    # Wait for the specified duration or until the song finishes
    start_time = time.time()
    while time.time() - start_time < play_duration:
        if not pygame.mixer.music.get_busy():
            break
        time.sleep(0.1)

    # while pygame.mixer.music.get_busy():
    #     pygame.time.wait(100)

    # Stop the song playback
    pygame.mixer.music.stop()

    # Quit Pygame mixer
    pygame.mixer.quit()


