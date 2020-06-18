from scipy import signal
import matplotlib.pyplot as plt
import numpy as np


def iir_bp_filter(source, left_lim, right_lim, samplerate):
    sos = signal.iirfilter(17, [left_lim, right_lim], rs=60, btype='bandpass', analog=False, ftype='cheby2', fs=samplerate, output='sos')
    w, h = signal.sosfreqz(sos, samplerate, fs=samplerate)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.semilogx(w, 20 * np.log10(np.maximum(abs(h), 1e-5)))
    ax.set_title('Characteristics IIR bandpass')
    ax.set_xlabel('Frequency [Hz]')
    ax.set_ylabel('Amplitude [dB]')
    ax.axis((10, 1000, -100, 10))
    ax.grid(which='both', axis='both')
    plt.show()

    return signal.sosfilt(sos, source)


def iir_bs_filter(source, left_lim, right_lim, samplerate):
    sos = signal.iirfilter(17, [left_lim, right_lim], rs=60, btype='bandstop', analog=False, ftype='cheby2', fs=samplerate, output='sos')
    w, h = signal.sosfreqz(sos, samplerate, fs=samplerate)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.semilogx(w, 20 * np.log10(np.maximum(abs(h), 1e-5)))
    ax.set_title('Characteristics IIR bandstop')
    ax.set_xlabel('Frequency [Hz]')
    ax.set_ylabel('Amplitude [dB]')
    ax.axis((10, 1000, -100, 10))
    ax.grid(which='both', axis='both')
    plt.show()

    return signal.sosfilt(sos, source)


def fir_bp_filter(source, left_lim, right_lim, samplerate):
    numtaps = int(samplerate/2)
    fil_taps = signal.firwin(numtaps, [left_lim, right_lim], fs=samplerate, pass_zero=False)
    w, h = signal.freqz(fil_taps, 1, worN=2000)
    plt.plot((samplerate * 0.5 / np.pi) * w, np.abs(h))
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Power")
    plt.title("FIR Bandpass Window")
    plt.show()

    return signal.lfilter(fil_taps, [1.0], source)


def fir_bs_filter(source, left_lim, right_lim, samplerate):
    numtaps = int(samplerate/2 + 1)
    fil_taps = signal.firwin(numtaps, [left_lim, right_lim], fs=samplerate)
    w, h = signal.freqz(fil_taps, 1, worN=2000)
    plt.plot((samplerate * 0.5 / np.pi) * w, np.abs(h))
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Power")
    plt.title("FIR Bandstop Window")
    plt.show()

    return signal.lfilter(fil_taps, [1.0], source)
