from gtts import gTTS
import os

def create_audio_files(names, directory):
    os.makedirs(directory, exist_ok=True)
    for name in names:
        tts = gTTS(name)
        file_path = os.path.join(directory, f"{name}.mp3")
        tts.save(file_path)

if __name__ == "__main__":
    with open('names.txt', 'r') as file:
        names_string = file.read()
        names = [name.strip() for name in names_string.split(',')]
    create_audio_files(names, './data')