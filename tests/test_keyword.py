import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from keywordlookup.keyword import KeywordLookup


class TestKeyword:
    keyword_lookup = KeywordLookup("test")

    def test_get_word_definitions(self):
        definitions = self.keyword_lookup.get_definitions()
        assert len(definitions) > 0 and isinstance(definitions, list)

    def test_get_pronunciations(self):
        pronunciations = self.keyword_lookup.get_pronunciations()
        
        assert pronunciations == (
            "https://audio.oxforddictionaries.com/en/mp3/test_us_1.mp3",
            "tɛst",
        )
