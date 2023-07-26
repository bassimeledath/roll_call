import os
import time
import pygame
import sys

def play_audio_files(directory, starting_name='', wait_time=5):
    pygame.mixer.init()
    all_files = [f for f in os.listdir(directory) if f.endswith('.mp3')]
    all_files.sort()
    starting_name = starting_name.lower()
    starting_file = None
    for f in all_files:
        if f.lower().startswith(starting_name):
            starting_file = f
            break
    if starting_file is not None:
        starting_index = all_files.index(starting_file)
        all_files = all_files[starting_index:]
    for filename in all_files:
        file_path = os.path.join(directory, filename)
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        print(f"Now calling: {filename[:-4]}")
        while pygame.mixer.music.get_busy():
            time.sleep(wait_time)

if __name__ == "__main__":
    directory = './data'
    starting_name = sys.argv[1] if len(sys.argv) > 1 else ''  # Use the first command-line argument as starting_name, or set it to an empty string if not provided
    play_audio_files(directory, starting_name)
