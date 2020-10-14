import numpy as np
import pandas as pd
import librosa
import os
import multiprocessing
from sklearn.model_selection import train_test_split
from keras import utils

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

    y, sr = librosa.load('Audio/{}.wav'.format(file_name))
    return(librosa.core.resample(y=y,orig_sr=sr,target_sr=RATE, scale=True))

def to_mfcc(wav_array):
    '''
    Converts wav file to Mel Frequency Ceptral Coefficients
    '''
    return(librosa.feature.mfcc(y=wav_array, sr=RATE, n_mfcc=N_MFCC))


def split_people(df,test_size=0.2):
    '''
    Create train test split of DataFrame
    '''

    return train_test_split(df['filename'],df['native_language'],test_size=test_size,random_state=1234)

def to_categorical(y):
    '''
    Converts list of languages into a binary class matrix
    '''
    lang_dict = {}
    for index,language in enumerate(set(y)):
        lang_dict[language] = index
    y = list(map(lambda x: lang_dict[x],y))
    return utils.to_categorical(y, len(lang_dict))

def make_segments(mfccs,labels):
    '''
    Makes segments of mfccs and attaches them to the labels
    '''
    segments = []
    seg_labels = []
    for mfcc,label in zip(mfccs,labels):
        for start in range(0, int(mfcc.shape[1] / COL_SIZE)):
            segments.append(mfcc[:, start * COL_SIZE:(start + 1) * COL_SIZE])
            seg_labels.append(label)
    return(segments, seg_labels)

df = pd.read_csv('Data/test.csv')
X_train, X_test, y_train, y_test = split_people(df)
pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
X_train = pool.map(get_wav, X_train)
X_test = pool.map(get_wav, X_test)
X_train = pool.map(to_mfcc, X_train)
X_test = pool.map(to_mfcc, X_test)
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)
X_train, y_train = make_segments(X_train, y_train)
X_validation, y_validation = make_segments(X_test, y_test)

print (X_train)
