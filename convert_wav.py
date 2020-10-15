import os
from pydub import AudioSegment

path = "Audio"
os.chdir(path)

audio_files = os.listdir()

for file in audio_files:
    name, ext = os.path.splitext(file)
    if ext == ".mp3":
       mp3_sound = AudioSegment.from_mp3(file)
       #rename them using the old name + ".wav"
       print(f"Converting {name}.mp3")
       mp3_sound.export("..\\WavFormat\\{0}.wav".format(name), format="wav")

print("CONVERSION DONE!!")
