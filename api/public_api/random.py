import requests
from api.public_api.public_api import PublicApi
from requests import Response


class Random(PublicApi):
    def get_random(self) -> Response:
        return requests.get(url=f"{self.url}/random")
