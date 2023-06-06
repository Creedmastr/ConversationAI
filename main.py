from functions import audiorecord
from functions import recognize
from functions import char
from functions import translation
import os
import so_vits_svc_fork

fs = 44100
seconds = 3
file_path = "./out/output.wav"
char_id = "eP9-QXMygAHz3xvWq8FZigmV8Rz_xozAtp3MEqzReYw"

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
