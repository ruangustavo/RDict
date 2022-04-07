import requests

from .config import OXFORD_API_ID, OXFORD_API_KEY

API_BASE_URL = "https://od-api.oxforddictionaries.com/api/v2/entries/en-us/{}"


class HttpClient:
    def __init__(self, api_id, api_key):
        self.api_id = api_id
        self.api_key = api_key

    def get(self, url):
        headers = {"app_id": self.api_id, "app_key": self.api_key}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise Exception(f"HTTP error: {err}")

        return response.json()

    def get_word_entries(self, word):
        url = self.url_builder(word, strictMatch=False)
        json = self.get(url)

        return [
            entry
            for result in json["results"]
            for lexical_entry in result["lexicalEntries"]
            for entry in lexical_entry["entries"]
        ]

    def url_builder(self, endpoint, **kwargs):
        url = API_BASE_URL.format(endpoint)

        if kwargs is not None:
            url += "?" + "&".join(f"{k}={v}" for k, v in kwargs.items())

        return url


class KeywordLookup:
    http = HttpClient(OXFORD_API_ID, OXFORD_API_KEY)

    def __init__(self, word):
        self.entries = self.http.get_word_entries(word)

    def get_definitions(self):
        definitions = []

        for entry in self.entries:
            for sense in entry["senses"]:
                if "definitions" in sense:
                    definitions.extend(sense["definitions"])

        return definitions

    def get_pronunciations(self):
        for entry in self.entries:
            for pronunciation in entry["pronunciations"][1]:
                if pronunciation["dialects"][0] == "American English":
                    audio_file = pronunciation["audioFile"]
                    phonetic_spelling = pronunciation["phoneticSpelling"]

        return (audio_file, phonetic_spelling)
