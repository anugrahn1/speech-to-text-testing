
import os
import uuid
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
import pygame

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
client = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)
pygame.mixer.init()

def text_to_speech_file(text: str) -> str:
    # Calling the text_to_speech conversion API with detailed parameters
    response = client.text_to_speech.convert(
        voice_id="Cx1no1fzyWp6JiZNaZLV", # Adam pre-made voice
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_turbo_v2", # use the turbo model for low latency, for other languages use the `eleven_multilingual_v2`
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
        ),
    )

    # uncomment the line below to play the audio back
    # play(response)

    # Generating a unique file name for the output MP3 file
    save_file_path = f"{uuid.uuid4()}.mp3"

    # Writing the audio to a file
    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"{save_file_path}: A new audio file was saved successfully!")

    # Return the path of the saved audio file
    return save_file_path


played_files = set()
# file_path = ''

def play_mp3_files(folder):
    global file_path
    files = os.listdir(folder)
    for file in files:
        if file.endswith('.mp3'):
            mp3_file = file
    
    file_path = os.path.join(folder, mp3_file)
    print(f"Playing {mp3_file}")

    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Check every 10 milliseconds for playback end


def return_file_path():
    global file_path
    return file_path

# Function to check for new MP3 files and play them
def play_new_mp3_files(folder):
    global played_files
    
    # Get a list of all files currently in the folder
    files = os.listdir(folder)
    mp3_files = [f for f in files if f.endswith('.mp3')]
    
    # Filter out files that have already been played
    new_files = [mp3_file for mp3_file in mp3_files if mp3_file not in played_files]

    # Play each new MP3 file once
    for mp3_file in new_files:
        file_path = os.path.join(folder, mp3_file)
        print(f"Playing: {mp3_file}")
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)  # Check every 10 milliseconds for playback end
        
        # Add the file to the set of played files
        played_files.add(mp3_file)
    
def delete_mp3_files(folder):
    files = os.listdir(folder)
    mp3_files = [f for f in files if f.endswith('.mp3')]

    for file in mp3_files: 
        os.remove(file)