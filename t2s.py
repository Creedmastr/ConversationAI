import speech_recognition as sr

def recognize_speech(path):
    r = sr.Recognizer()

    with sr.AudioFile(path) as file:
        audio = r.record(file)
    
    text = r.recognize_google(audio)
    print(text)
    
    


