import speech_recognition as sr
from speech_recognition.exceptions import UnknownValueError
from functions.panic import panic
import os

def recognize_speech(path):
    print("INFO: Recognizing speech")

    r = sr.Recognizer()

    with sr.AudioFile(path) as file:
        audio = r.record(file)
    
    try:
        text = r.recognize_google(audio)
    except UnknownValueError as err:
        panic("No speech recognized in the record.")
    
    os.remove('./out/output.wav')

    return text
