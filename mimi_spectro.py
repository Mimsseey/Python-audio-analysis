 import os
 os.getcwd()
'C:\\Windows\\system32'
 os.chdir(r"C:\Users\Miha\Desktop\py")
 import librosa
 import librosa.display
 import numpy as np
 import matplotlib.pyplot as plt
 import IPython.display as ipd
 mimi_wav = "mimi.wav"
 y, sr = librosa.load(mimi_wav, sr=None, mono=True)
 print(type(y), type(sr))
 class 'numpy.ndarray'> <class 'int'>
 print(y.shape, sr)
(340609,) 48000
 plt.figure(figsize=(14, 5))
 Figure size 1400x500 with 0 Axes>
 librosa.display.waveplot(y, sr=sr)
 plt.show()
 n_fft = 2048
 D = np.abs(librosa.stft(y[:n_fft], n_fft=n_fft, hop_length=n_fft+1))
 plt.plot(D);
 plt.show()
 plt.colorbar();
 plt.show()
 DB = librosa.amplitude_to_db(D, ref=np.max)
 librosa.display.specshow(DB, sr=sr, hop_length=hop_length, x_axis='time', y_axis='log');
 plt.colorbar(format='%+2.0f dB');
 plt.show()
