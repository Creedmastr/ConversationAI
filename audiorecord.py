import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(ouput, sample_rate, duration):
    myrecording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()
    write(ouput, sample_rate, myrecording)