import signal_analysis
import file_manipulation as f_man


def main():
    f_man.generate_wav_from_string("oleksandr")

    data, samplerate = f_man.read_wav_from_file()

    signal_analysis.spectrum(data, samplerate)
    signal_analysis.spectrogram(data)


main()


