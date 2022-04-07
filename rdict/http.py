import requests


class HttpClient:
    def __init__(self, api, headers=None):
        self.API = api
        self.session = requests.Session()

        if headers is not None:
            self.session.headers.update(headers)

    def get_content(self, url):
        try:
            response = self.session.get(url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise Exception(err)

        return response.json()

    def get_url(self, endpoint, **kwargs):
        url = self.API.format(endpoint)

        if kwargs:
            url += "?" + "&".join(f"{k}={v}" for k, v in kwargs.items())

        return url
