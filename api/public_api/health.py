import requests
from api.public_api.public_api import PublicApi
from requests import Response


class Health(PublicApi):
    def get_health(self) -> Response:
        return requests.get(url=f"{self.url}/health")
