from gtts import gTTS

def speak(text, output_file):
    tts = gTTS(text=text, lang='ja')
    tts.save(output_file)
