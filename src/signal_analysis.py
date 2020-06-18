import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def spectrum(data, fs):
    fft_res = np.fft.fft(data, int(len(data) - len(data) / 2))
    wave_freqs = np.fft.fftfreq(len(fft_res)) * fs

    figure = plt.figure()
    widmo = figure.add_subplot(111)
    widmo.set(xlabel="Frequency [Hz]", ylabel="Power [dB]", title=title)
    # To convert signal magnitude to decibel use the following formula
    # db = 20 * log10(Magnitude)
    widmo.plot(wave_freqs[:int(len(wave_freqs) / 2)], 20 * np.log10(fft_res)[:int(len(fft_res) / 2)])
    plt.show()


def spectrogram(yaxis):
    my = np.array(yaxis)
    f, t, Sxx = signal.spectrogram(my, 44100)
    plt.pcolormesh(t, f, Sxx)
    plt.xlabel('Time [Sec]')
    plt.ylabel('Frequency [Hz]')
    plt.title('Spektrogram sygnału')
    plt.show()
