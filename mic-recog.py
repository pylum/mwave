from mwave.utils import get_mic_phrase
from mwave.audio import MAudio

audio = MAudio(get_mic_phrase())

print('Sample duration %.2f' % (audio.duration))
