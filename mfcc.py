import numpy as np
import pandas as pd
import librosa
import os

DEBUG = True
SILENCE_THRESHOLD = .01
RATE = 24000
N_MFCC = 13
COL_SIZE = 30
EPOCHS = 10

def get_wav(file_name):
    '''
    Load wav file from disk and down-samples to RATE
    '''

    y, sr = librosa.load('../Audio/{}.wav'.format(file_name))
    return(librosa.core.resample(y=y,orig_sr=sr,target_sr=RATE, scale=True))

def to_mfcc(wav_array):
    '''
    Converts wav file to Mel Frequency Ceptral Coefficients
    '''
    return(librosa.feature.mfcc(y=wav_array, sr=RATE, n_mfcc=N_MFCC))

wav_array = get_wav('arabic1')
mfcc = to_mfcc(wav_array)
