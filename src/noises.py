import file_manipulation


noises_paths = ['./noises/brown.wav',
                './noises/pink.wav',
                './noises/white.wav']


def get_brown_noise():
    noise_data, samplerate = file_manipulation.read_wav_from_file(filename=noises_paths[0])

    return noise_data


def get_pink_noise():
    noise_data, samplerate = file_manipulation.read_wav_from_file(filename=noises_paths[1])

    return noise_data


def get_white_noise():
    noise_data, samplerate = file_manipulation.read_wav_from_file(filename=noises_paths[2])

    return noise_data


