from rdict.config import OXFORD_API_ID, OXFORD_API_KEY
from rdict.dictionary import DictBase
from rdict.http import HttpClient


class OxfordDictionary(DictBase):
    API = "https://od-api.oxforddictionaries.com/api/v2/entries/en-us/{}"

    def __init__(self):
        self.http = HttpClient(
            self.API, headers={"app_id": OXFORD_API_ID, "app_key": OXFORD_API_KEY}
        )

    def show(self):
        for index, definition in enumerate(self.definitions, start=1):
            print(f"{index} - {definition}")

    def query(self, word):
        self.entries = self.get_entries(word)
        self.definitions = self.get_definitions()
        self.pronunciation_spelling = self.get_pronunciation_spelling()
        self.pronunciation_audio = self.get_pronunciation_audio()

    def get_entries(self, word):
        url = self.http.get_url(word, strictMatch=False)
        json = self.http.get(url)

        return [
            entry
            for result in json["results"]
            for lexical_entry in result["lexicalEntries"]
            for entry in lexical_entry["entries"]
        ]

    def get_definitions(self):
        definitions = []

        for entry in self.entries:
            for sense in entry["senses"]:
                if "definitions" in sense:
                    definitions.extend(sense["definitions"])

        return definitions

    def get_pronunciation_spelling(self):
        for entry in self.entries:
            if "pronunciations" in entry:
                for pronunciation in entry["pronunciations"]:
                    if (
                        pronunciation["phoneticNotation"] == "IPA"
                        and pronunciation["dialects"][0] == "American English"
                    ):
                        return pronunciation["phoneticSpelling"]

    def get_pronunciation_audio(self):
        for entry in self.entries:
            if "pronunciations" in entry:
                for pronunciation in entry["pronunciations"]:
                    if "audioFile" in pronunciation:
                        return pronunciation["audioFile"]
