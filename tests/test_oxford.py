import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rdict.dictionaries.oxford import OxfordDictionary


class TestOxford:
    oxford = OxfordDictionary()

    def test_get_url_without_params(self):
        url = self.oxford.API.format("string")
        assert self.oxford.http.get_url("string") == url

    def test_get_url_with_params(self):
        url = self.oxford.API.format("string") + "?strictMatch=false"
        assert self.oxford.http.get_url("string", strictMatch="false") == url

    def test_get_word_definitions(self):
        self.oxford.query("string")
        assert len(self.oxford.definitions) > 0

    def test_get_pronunciation_spelling(self):
        self.oxford.query("string")
        assert self.oxford.pronunciation_spelling == "strɪŋ"

    def test_get_pronunciation_audio(self):
        self.oxford.query("string")
        assert (
            self.oxford.pronunciation_audio
            == "https://audio.oxforddictionaries.com/en/mp3/string_us_1.mp3"
        )
