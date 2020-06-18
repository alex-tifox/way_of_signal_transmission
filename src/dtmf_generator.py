# Algorithm
# Get string
# Loop through the string
# For the chars 0-9, ABCD, * # generate waves with required frequency

# |-----------------------------------------------|
# |    1    |    2    |    3    |    A    | 697 Hz |
# |---------|---------|---------|---------|--------|
# |    4    |    5    |    6    |    B    | 770 Hz |
# |---------|---------|---------|---------|--------|
# |    7    |    8    |    9    |    C    | 852 Hz |
# |---------|---------|---------|---------|--------|
# |    *    |    0    |    #    |    D    | 941 Hz |
# |---------|---------|---------|---------|--------|
# | 1209 Hz | 1336 Hz | 1477 Hz | 1633 Hz |
# |---------------------------------------|

import numpy as np

# GLOBAL VARS
T = 0.1
fs = 44100


def dtmf_generator(string_to_encode):
    string_to_encode = dtmf_encode_string_to_signal(string_to_encode)

    result = np.empty(shape=0)
    start_time = 0
    end_time = T

    for char in string_to_encode:
        if char == '1':
            result = np.append(result,
                               generate_wave_with_parameters(start_time=start_time, end_time=end_time, f1=697, f2=1209))
        elif char == '2':
            result = np.append(result,
                               generate_wave_with_parameters(start_time=start_time, end_time=end_time, f1=697, f2=1336))
        elif char == '3':
            result = np.append(result,
                               generate_wave_with_parameters(start_time=start_time, end_time=end_time, f1=697, f2=1477))
        elif char == '4':
            result = np.append(result,
                               generate_wave_with_parameters(start_time=start_time, end_time=end_time, f1=770, f2=1209))
        elif char == '5':
            result = np.append(result,
                               generate_wave_with_parameters(start_time=start_time, end_time=end_time, f1=770, f2=1336))
        elif char == '6':
            result = np.append(result,
                               generate_wave_with_parameters(start_time=start_time, end_time=end_time, f1=770, f2=1477))
        elif char == '7':
            result = np.append(result,
                               generate_wave_with_parameters(start_time=start_time, end_time=end_time, f1=852, f2=1209))
        elif char == '8':
            result = np.append(result,
                               generate_wave_with_parameters(start_time=start_time, end_time=end_time, f1=852, f2=1336))
        elif char == '9':
            result = np.append(result,
                               generate_wave_with_parameters(start_time=start_time, end_time=end_time, f1=852, f2=1477))
        elif char == '0':
            result = np.append(result,
                               generate_wave_with_parameters(start_time=start_time, end_time=end_time, f1=941, f2=1366))
        elif char == 'A':
            result = np.append(result,
                               generate_wave_with_parameters(start_time=start_time, end_time=end_time, f1=697, f2=1633))
        elif char == 'B':
            result = np.append(result,
                               generate_wave_with_parameters(start_time=start_time, end_time=end_time, f1=770, f2=1633))
        elif char == 'C':
            result = np.append(result,
                               generate_wave_with_parameters(start_time=start_time, end_time=end_time, f1=852, f2=1633))
        elif char == 'D':
            result = np.append(result,
                               generate_wave_with_parameters(start_time=start_time, end_time=end_time, f1=852, f2=1633))
        elif char == '*':
            result = np.append(result,
                               generate_wave_with_parameters(start_time=start_time, end_time=end_time, f1=941, f2=1209))
        elif char == '#':
            result = np.append(result,
                               generate_wave_with_parameters(start_time=start_time, end_time=end_time, f1=941, f2=1633))

        # print('Start and end time are: ', start_time, end_time)
        start_time += T
        end_time += T

    return result


# private method
def dtmf_encode_string_to_signal(string_to_encode):
    string_to_encode = str.lower(string_to_encode)
    result_string_for_dtmf_generation = ''
    for char in string_to_encode:
        if char == 'a':
            result_string_for_dtmf_generation += '2'
        elif char == 'b':
            result_string_for_dtmf_generation += '22'
        elif char == 'c':
            result_string_for_dtmf_generation += '222'
        elif char == 'd':
            result_string_for_dtmf_generation += '3'
        elif char == 'e':
            result_string_for_dtmf_generation += '33'
        elif char == 'f':
            result_string_for_dtmf_generation += '333'
        elif char == 'g':
            result_string_for_dtmf_generation += '4'
        elif char == 'h':
            result_string_for_dtmf_generation += '44'
        elif char == 'i':
            result_string_for_dtmf_generation += '444'
        elif char == 'j':
            result_string_for_dtmf_generation += '5'
        elif char == 'k':
            result_string_for_dtmf_generation += '55'
        elif char == 'l':
            result_string_for_dtmf_generation += '555'
        elif char == 'm':
            result_string_for_dtmf_generation += '6'
        elif char == 'n':
            result_string_for_dtmf_generation += '66'
        elif char == 'o':
            result_string_for_dtmf_generation += '666'
        elif char == 'p':
            result_string_for_dtmf_generation += '7'
        elif char == 'q':
            result_string_for_dtmf_generation += '77'
        elif char == 'r':
            result_string_for_dtmf_generation += '777'
        elif char == 's':
            result_string_for_dtmf_generation += '7777'
        elif char == 't':
            result_string_for_dtmf_generation += '8'
        elif char == 'u':
            result_string_for_dtmf_generation += '88'
        elif char == 'v':
            result_string_for_dtmf_generation += '888'
        elif char == 'w':
            result_string_for_dtmf_generation += '9'
        elif char == 'x':
            result_string_for_dtmf_generation += '99'
        elif char == 'y':
            result_string_for_dtmf_generation += '999'
        elif char == 'z':
            result_string_for_dtmf_generation += '9999'
        elif char == ' ' or char == '_':
            result_string_for_dtmf_generation += '0'

    return result_string_for_dtmf_generation


#private method
def generate_wave_with_parameters(start_time=0, end_time=1, amplitude=2, sample_rate=fs, f1=2, f2=3, phi=0):
    t = np.linspace(start_time, end_time, int((end_time - start_time) * sample_rate))
    return_signal = np.array(amplitude * (np.sin(2 * np.pi * t * f1 + phi))) + np.array(amplitude * np.sin(2 * np.pi * t * f2 + phi))

    return return_signal
