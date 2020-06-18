import signal_analysis
import file_manipulation as f_man
import matplotlib.pyplot as plt


def main():
    f_man.generate_wav_from_string("oleksandr")

    data, samplerate = f_man.read_wav_from_file()

    signal_analysis.spectrum(data, samplerate)
    plt.show()
    signal_analysis.spectrogram(data)

    signal_analysis.add_noise_to_signal(data, "brown", samplerate, 0.15)
    signal_analysis.add_noise_to_signal(data, "brown", samplerate, 0.5)
    signal_analysis.add_noise_to_signal(data, "brown", samplerate, 0.85)

    signal_analysis.add_noise_to_signal(data, "pink", samplerate, 0.15)
    signal_analysis.add_noise_to_signal(data, "pink", samplerate, 0.5)
    signal_analysis.add_noise_to_signal(data, "pink", samplerate, 0.85)

    signal_analysis.add_noise_to_signal(data, "white", samplerate, 0.15)
    signal_analysis.add_noise_to_signal(data, "white", samplerate, 0.5)
    signal_analysis.add_noise_to_signal(data, "white", samplerate, 0.85)


main()


