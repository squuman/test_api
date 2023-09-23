from api.public_api.public_api import PublicApi
from requests import Response
from requests import get


class Categories(PublicApi):
    def get_categories(self) -> Response:
        return get(url=f"{self.url}/categories")
