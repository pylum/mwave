from speech_recognition import Microphone

from .audio import AUDIO_FORMAT
from .audio import AUDIO_FRAMES_PER_BUFFER


class MMicrofone(Microphone):
    def __init__(self, device_index=None, sample_rate=None, chunk_size=AUDIO_FRAMES_PER_BUFFER, format=AUDIO_FORMAT):
        super(MMicrofone, self).__init__(device_index, sample_rate, chunk_size)
        self.format = format
