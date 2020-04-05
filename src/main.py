# author - to42192 - Oleksandr Tilnyi
# Python 3.7

from pysndfile import *
import pysndfile

import matplotlib.pyplot as plt
import numpy as np
import os

mydir = os.path.dirname(__file__)

# Get the object of .wav sound file
wav = PySndfile(os.path.join(mydir, 'test_sample.wav'))
print(wav)

wav.rewind()  # 1-1

# Read data of sound - 230 000 frames of it
wav_data = wav.read_frames(nframes=230000)  # 2-1
# wav.rewind() # 2-1

# Creating object of new sound, mode to read/write, format and others - like in the original sound
wav_to_write = PySndfile(filename=os.path.join(mydir, 'test_sample_written.wav'), mode='rw', format=wav.format(),
                         channels=wav.channels(), samplerate=wav.samplerate())

print(wav_to_write)

# Write part of the original .wav to the new one
wav_to_write.write_frames(wav_data)  # 1-2
print(wav_to_write)

# Graphs
###
plt.title('Sound that will be written to the new .wav')
plt.plot(wav_data)
plt.show()
###
plt.title('2000 first frames of newly created .wav')
plt.plot(wav_to_write.read_frames(nframes=2000))
plt.show()
###
