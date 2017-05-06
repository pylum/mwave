from mwave.utils import get_mic_phrase

from config import settings

audio_format = settings.default_audio_format
file_name = settings.default_audio_file_name + '.' + audio_format

audio_data = get_mic_phrase()
with open(file_name, 'wb') as f:
    f.write(getattr(audio_data, 'get_'+audio_format + '_data')())
