import numpy as np
import pyaudio
from scipy.io import wavfile

AUDIO_FORMAT = pyaudio.paInt16
AUDIO_FRAMES_PER_BUFFER = 1024
AUDIO_RATE = 44100


class MAudio():
    def __init__(self, audio_data):
        self.sample_rate = audio_data.sample_rate
        self.data = np.fromstring(audio_data.frame_data, dtype=np.int16)
        self.duration = self.data.size / self.sample_rate

    def from_wav_file(self, file_name):
        self.sample_rate, self.data = wavfile.read(file_name)
        self.duration = self.data.size / self.sample_rate
        return self
