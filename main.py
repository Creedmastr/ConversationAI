import audiorecord
import t2s
import api_token

fs = 44100
seconds = 3
file_path = "output.wav"

audiorecord.record_audio(file_path, fs, seconds)
t2s.recognize_speech(file_path)

