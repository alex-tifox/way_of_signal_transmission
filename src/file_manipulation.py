import soundfile
import dtmf_generator as dgen


def generate_wav_from_string(string):
    wav_data = dgen.dtmf_generator(string)
    soundfile.write('dtmf_from_string.wav', wav_data, 44100)

    return wav_data


def read_wav_from_file(filename='dtmf_from_string.wav'):
    wav_data, samplerate = soundfile.read(filename)

    return wav_data, samplerate
