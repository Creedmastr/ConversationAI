from gtts import gTTS
from pydub import AudioSegment
import os

def speak(text, output_file):
    tts = gTTS(text=text, lang='ja')
    tts.save(output_file)

    audio = AudioSegment.from_file(output_file)
    audio.export(output_file, format="wav")
