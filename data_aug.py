import numpy as np
from scipy.io.wavfile import write
import librosa
import os

path = "deletethis" #or whichever source folder
os.chdir(path)

def load_audio_file(file_path):
    input_length = 1159168       
    data = librosa.core.load(file_path)[0] 
    if len(data)>input_length:
        data = data[:input_length]
    else:
        data = np.pad(data, (0, max(0, input_length - len(data))), "constant")
    return data

def stretch(data, rate=1):
    input_length = 1159168
    data = librosa.effects.time_stretch(data, rate)
    if len(data)>input_length:
        data = data[:input_length]
    else:
        data = np.pad(data, (0, max(0, input_length - len(data))), "constant")

    return data

def manipulate(data, sampling_rate, pitch_factor):
    return librosa.effects.pitch_shift(data, sampling_rate, pitch_factor)

audio_files = os.listdir()

for file in audio_files:
    name, ext = os.path.splitext(file)
    data = load_audio_file(file)
    wn = np.random.randn(len(data))
    data_wn1 = data + 0.005*wn
    write("C:\\Users\\Navyasree\\Accent-Classification\\andthis\\{0}_wn1.wav".format(name), 24100, data_wn1) #change path
    data_roll1 = np.roll(data, 1600)
    write("C:\\Users\\Navyasree\\Accent-Classification\\andthis\\{0}_roll1.wav".format(name), 24100, data_roll1)
    data_stretch =stretch(data, 0.8)
    write("C:\\Users\\Navyasree\\Accent-Classification\\andthis\\{0}_stretch1.wav".format(name), 24100, data_stretch)
    data_stretch2 =stretch(data, 1.2)
    write("C:\\Users\\Navyasree\\Accent-Classification\\andthis\\{0}_stretch2.wav".format(name), 24100, data_stretch2)
    data_wn2 = data + 0.0009*wn
    write("C:\\Users\\Navyasree\\Accent-Classification\\andthis\\{0}_wn2.wav".format(name), 24100, data_wn2)
    data_roll2 = np.roll(data, 90000)
    write("C:\\Users\\Navyasree\\Accent-Classification\\andthis\\{0}_roll2.wav".format(name), 24100, data_roll2)
    data_pitch1 = manipulate(data, 24100, 0.1)
    write("C:\\Users\\Navyasree\\Accent-Classification\\andthis\\{0}_pitch1.wav".format(name), 24100, data_pitch1)
    data_pitch2 = manipulate(data, 24100, 0.2)
    write("C:\\Users\\Navyasree\\Accent-Classification\\andthis\\{0}_pitch2.wav".format(name), 24100, data_pitch2)