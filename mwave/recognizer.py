from speech_recognition import Recognizer
from speech_recognition import UnknownValueError

from mwave import hidden_markov


class MRecognizer(Recognizer):
    def __init__(self):
        super(MRecognizer, self).__init__()

    def recognize_marcov(self, audio_data, language="en-US", show_all=False):
        """
        Performs speech recognition on ``audio_data`` (an numpy array), using Markov Chain Algorithm.

        Returns the most likely transcription if ``show_all`` is false (the default).
        Otherwise, returns the Markov ``mwave.hidden_markov.Decoder`` object resulting from the recognition.

        Raises a ``speech_recognition.UnknownValueError`` exception if the speech is unintelligible.
        """

        decoder = hidden_markov.Decoder(audio_data)
        decoder.process_raw()

        if show_all:
            return decoder

        # return results
        hypothesis = decoder.hyp()
        if hypothesis is None:
            raise UnknownValueError()

        return hypothesis.hypstr
