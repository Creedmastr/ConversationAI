py main.py
cd rvc
py inference.py 
Add-Type -AssemblyName presentationCore
(New-Object Media.SoundPlayer "./rvc/audio-outputs/output.wav").PlaySync();
