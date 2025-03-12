import os
from groq import Groq

# Initialize the Groq client
client = Groq()

# Specify the path to the audio file
filename = os.path.dirname(__file__) + "/Realidade Virtual.mp3" # Replace with your audio file!

# Open the audio file
with open(filename, "rb") as file:
    # Create a transcription of the audio file
    transcription = client.audio.transcriptions.create(
      file=(filename, file.read()), # Required audio file
      model="whisper-large-v3-turbo", # Required model to use for transcription
      prompt="Áudio",  # Optional
      response_format="verbose_json",  # Optional
      language="pt",  # Optional
      temperature=0.0  # Optional
    )
    # Print the transcription text
    print(transcription.text)