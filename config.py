from addict import Dict

settings = Dict()

settings.default_audio_format = 'wav'
settings.default_audio_file_name = 'audio_sample'

settings.calibrate_duration = 1
settings.audio_formats = ('raw', 'wav', 'aiff', 'flac')



# api keys, see https://github.com/Uberi/speech_recognition for details

settings.api_key.google = ''