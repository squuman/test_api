from api.public_api.public_api import PublicApi
from requests import Response
from requests import get, post


class Entries(PublicApi):
    def get_entries(self) -> Response:
        return get(url=f"{self.url}/entries")
