#**This code is a mix of examples from [blog] (https://towardsdatascience.com/extract-features-of-music-75a3f9bc265d) & [Librosa package site] (https://librosa.org/)**#


import os
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import IPython.display as ipd
#change directory to where wav files are located
os.chdir(r"C:\Users\XXXX\")

mimi_mjau = "TEST_mimi.wav" #import wav file
y, sr = librosa.load(mimi_mjau,) 
plt.figure(figsize=(15, 6))
librosa.display.waveplot(y, sr=sr)
plt.show()
n_fft = 2048
D = np.abs(librosa.stft(y[:n_fft], n_fft=n_fft, hop_length=n_fft+1))
plt.plot(D)
plt.show()
DB = librosa.amplitude_to_db(D, ref=np.max)
librosa.display.specshow(DB, sr=sr, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.show()
