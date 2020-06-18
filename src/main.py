import signal_analysis
import file_manipulation as f_man
import matplotlib.pyplot as plt

import filters


def main():
    f_man.generate_wav_from_string("olek")

    data, samplerate = f_man.read_wav_from_file()

    signal_analysis.spectrum(data, samplerate)
    plt.show()
    signal_analysis.spectrogram(data)

    # signal_analysis.add_noise_to_signal(data, "brown", samplerate, 0.15)
    # noised_signal_b = signal_analysis.add_noise_to_signal(data, "brown", samplerate, 0.5)
    # signal_analysis.add_noise_to_signal(data, "brown", samplerate, 0.85)
    #
    # signal_analysis.add_noise_to_signal(data, "pink", samplerate, 0.15)
    # noised_signal_p = signal_analysis.add_noise_to_signal(data, "pink", samplerate, 0.5)
    # signal_analysis.add_noise_to_signal(data, "pink", samplerate, 0.85)

    # signal_analysis.add_noise_to_signal(data, "white", samplerate, 0.15)

    noised_signal_w = signal_analysis.add_noise_to_signal(data, "white", samplerate, 0.5)

    # signal_analysis.add_noise_to_signal(data, "white", samplerate, 0.85)


    # filtered = filters.iir_bp_filter(noised_signal_b, 640, 1550, samplerate)
    # signal_analysis.spectrum(filtered, samplerate)
    # plt.show()
    # filtered = filters.iir_bp_filter(noised_signal_p, 640, 1550, samplerate)
    # signal_analysis.spectrum(filtered, samplerate)
    # plt.show()

    filtered = filters.iir_bp_filter(noised_signal_w, 640, 1550, samplerate)
    signal_analysis.spectrum(filtered, samplerate)
    plt.show()

    #
    # filtered = filters.iir_bs_filter(noised_signal_b, 640, 1550, samplerate)
    # signal_analysis.spectrum(filtered, samplerate)
    # plt.show()
    # filtered = filters.iir_bs_filter(noised_signal_p, 640, 1550, samplerate)
    # signal_analysis.spectrum(filtered, samplerate)
    # plt.show()
    # filtered = filters.iir_bs_filter(noised_signal_w, 640, 1550, samplerate)
    # signal_analysis.spectrum(filtered, samplerate)
    # plt.show()
    #
    # filtered = filters.fir_bp_filter(noised_signal_b, 640, 1550, samplerate)
    # signal_analysis.spectrum(filtered, samplerate)
    # plt.show()
    # filtered = filters.fir_bp_filter(noised_signal_p, 640, 1550, samplerate)
    # signal_analysis.spectrum(filtered, samplerate)
    # plt.show()
    # filtered = filters.fir_bp_filter(noised_signal_w, 640, 1550, samplerate)
    # signal_analysis.spectrum(filtered, samplerate)
    # plt.show()
    #
    # filtered = filters.fir_bs_filter(noised_signal_b, 640, 1550, samplerate)
    # signal_analysis.spectrum(filtered, samplerate)
    # plt.show()
    # filtered = filters.fir_bs_filter(noised_signal_p, 640, 1550, samplerate)
    # signal_analysis.spectrum(filtered, samplerate)
    # plt.show()
    # filtered = filters.fir_bs_filter(noised_signal_w, 640, 1550, samplerate)
    # signal_analysis.spectrum(filtered, samplerate)
    # plt.show()

    plt.plot(filtered)
    plt.show()

    signal_analysis.spectrogram(filtered)


main()


