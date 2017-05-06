from config import settings
from mwave.microfone import MMicrofone
from mwave.recognizer import MRecognizer


def get_mic_phrase(pre_msg='Say something, please', post_msg='Recorded!'):
    recognizer = MRecognizer()
    with MMicrofone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=settings.calibrate_duration)

        print(pre_msg)
        audio = recognizer.listen(source)
        print(post_msg)

    return audio
