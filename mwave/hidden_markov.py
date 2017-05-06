LANGUAGE_DIRECTORY = "hidden_markov_data"
ACCOUSTIC_MODEL = "hidden_markov_model"
LANGUAGE_MODEL_FILE = "language-model.bin"
PHONEME_FILE = "pronounciation-dictionary.bin"


class Decoder(object):
    def __init__(self, raw_data):
        self.raw_data = raw_data

    def process_raw(self):
        pass

    def hyp(self):
        pass
