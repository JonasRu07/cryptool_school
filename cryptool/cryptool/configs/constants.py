import json
import os

class CaeserAlphabets:
    def __init__(self, lang:str='DE', path:str = os.path.join('cryptool', 'cryptool', 'configs', 'caeser')):
        self._language = lang
        self._alphabet = []
        self._frequency_alphabet = []

        self._reinit(path)

    def _reinit(self, path):
        with open(os.path.join(path, 'alphabet.json')) as file:
            self._alphabet = json.load(file)['DE']
        with open(os.path.join(path, 'frequency_alphabet.json')) as file:
            self._frequency_alphabet = json.load(file)['DE']

    @property
    def alphabet(self): return self._alphabet

    @property
    def frequency_alphabet(self): return self._frequency_alphabet

