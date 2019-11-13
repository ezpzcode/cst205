import numpy as np

# cd audio at 44,100 hz and 16 bits per sample
SAMPLES_S = 44_100
BITS_SAMPLE = 16


# wave header constants
CHUNK_ID = b'RIFF'
FORMAT = b'WAVE'
SUBCHUNK_1_ID = b'fmt '
SUBCHUNK_2_ID = b'data'

# PCM constants
SUBCHUNK_1_SIZE = (16).to_bytes(4, byteorder='little')
AUDIO_FORMAT = (1).to_bytes(2, byteorder='little')

def create_pcm(frequency, frequency1,frequency2,frequency3,frequency4):
    ang_freq1 = 2*np.pi*frequency
    x_vals1 = np.arange(SAMPLES_S)
    ang_freq2 = 2*np.pi*frequency1
    x_vals2 = np.arange(SAMPLES_S)
    ang_freq3 = 2*np.pi*frequency2
    x_vals3 = np.arange(SAMPLES_S)
    ang_freq4 = 2*np.pi*frequency3
    x_vals4 = np.arange(SAMPLES_S)
    ang_freq5 = 2*np.pi*frequency4
    x_vals5 = np.arange(SAMPLES_S)

    y_vals = ((32767 * .3 * np.sin(ang_freq1 * x_vals1 / SAMPLES_S))+(32767 * .3 * np.sin(ang_freq2 * x_vals2 / SAMPLES_S))+(32767 * .3 * np.sin(ang_freq3 * x_vals3 / SAMPLES_S))+(32767 * .3 * np.sin(ang_freq4 * x_vals4 / SAMPLES_S))+(32767 * .3 * np.sin(ang_freq5 * x_vals5 / SAMPLES_S))) / 5
    return np.int16(y_vals)

def new_wav(channels, filename, *args):
    seconds = len(args)

    chunk_size = (int(36 + (seconds * SAMPLES_S * BITS_SAMPLE/8))).to_bytes(4, 'little')
    num_channels = (channels).to_bytes(2, byteorder='little')
    sample_rate = (SAMPLES_S).to_bytes(4, byteorder='little')
    byte_rate = (int(SAMPLES_S * channels * BITS_SAMPLE/8)).to_bytes(4, byteorder='little')
    block_align = (int(channels * BITS_SAMPLE/8)).to_bytes(2, byteorder='little')
    bits_per_sample = (BITS_SAMPLE).to_bytes(2, byteorder='little')
    subchunk_2_size = (int(seconds * SAMPLES_S * BITS_SAMPLE/8)).to_bytes(4, byteorder='little')

    my_pcm = []

    for arg in args:
        my_pcm.append(create_pcm(arg[0],arg[1],arg[2],arg[3],arg[4]))

    mat = np.array(my_pcm)

    with open(f'{filename}.wav', 'wb') as fo:
        fo.write(
            CHUNK_ID +
            chunk_size +
            FORMAT +
            SUBCHUNK_1_ID +
            SUBCHUNK_1_SIZE +
            AUDIO_FORMAT +
            num_channels +
            sample_rate +
            byte_rate +
            block_align +
            bits_per_sample +
            SUBCHUNK_2_ID +
            subchunk_2_size +
            mat.tobytes()
        )

new_wav(1,'task4', (329.63, 415.30, 493.88, 587.33, 698.46))