from functions import audiorecord
from functions import recognize
from functions import char
from functions import translation
from functions import t2s
import os

fs = 44100
seconds = 3
file_path = "./out/output.wav"
char_id = "0NJqYQYuB8SEHHKzh2qHYzvMSMrlgWSlJldNXi8TTPs"

question = input('Add question mark? Yes by default')

if not os.path.exists('./out/'):
    os.mkdir('./out/')

audiorecord.record_audio(file_path, fs, seconds)
speech = recognize.recognize_speech(file_path)

if not question == 'y' or not question == 'yes':
    speech = speech + '?'

print(speech)

answer = char.get_answer(char_id, speech)
translated_text = translation.translate(answer['replies'][0]['text'], 'en', 'ja')

print(f'Character: {answer["src_char"]["participant"]["name"]}')
print("ENGLISH: ")
print(answer['replies'][0]['text'])
print("JAPANESE: ")
print(translated_text)

t2s.speak(translated_text, './out/speaked_base.mp3')

