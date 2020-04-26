# author - to42192 - Oleksandr Tilnyi
# Python 3.7

from pysndfile import *
import pysndfile

import matplotlib.pyplot as plt
import numpy as np
import os

import dtmf_generator
from dtmf_generator import dtmf_encode_string_to_signal as encode_string

# GLOBAL VARS
# --------------
mydir = os.path.dirname(__file__)
# --------------


def get_object_to_read(filename):
    return PySndfile(os.path.join(mydir, filename))


def read_frames_from_wav(filename, nframes=-1):
    # Get the object of .wav sound file
    wav = PySndfile(os.path.join(mydir, filename))

    # Read data of sound - 230 000 frames of it
    return wav.read_frames(nframes)


def write_signal_to_file(filename_to_write, data, mode, format, channels, samplerate):
    wav_to_write = PySndfile(filename=os.path.join(mydir, filename_to_write), mode=mode, format=format,
              channels=channels, samplerate=samplerate)

    wav_to_write.write_frames(data)

    return wav_to_write


dtmf_data = dtmf_generator.dtmf_generator(encode_string('a'))
# Creating object of new sound, mode to read/write, format and others - like in the original sound

arr = dtmf_generator.divide_to_borders(dtmf_data)
plt.plot(dtmf_data)
plt.show()
# dtmf_generator.spectrogram(arr)
dtmf_generator.noised_signal_spectrum_spectrogram(dtmf_data)

# # Write part of the original .wav to the new one
# wav_to_write = write_signal_to_file('test_sample_written.wav', dtmf_data, 'rw', get_object_to_read('test_sample.wav').format(), 1, dtmf_generator.fs)  # 1-2
# print(wav_to_write)
#
# # Graphs
# ###
# plt.title('Sound that will be written to the new .wav')
# plt.plot(dtmf_data)
# plt.show()
# ###
# plt.title('Frames of newly created .wav')
# plt.plot(wav_to_write.read_frames())
# plt.show()
# ###
