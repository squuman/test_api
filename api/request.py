import requests

from pydantic import BaseModel
from typing import Optional, Union


class Request:
    url: str
    headers: dict = {}
    data: dict
    files: dict
    json: dict
    params: dict

    def __new__(cls, *args, **kwargs):
        obj = super(Request, cls).__new__(cls)

        for attr in ['data', 'json', 'params', 'files']:
            obj.__setattr__(attr, {})

        obj.__init__(*args, **kwargs)

        return obj

    def request(
            self,
            url: str,
            headers: Optional[dict] = None,
            data: Optional[Union[dict, list, BaseModel]] = None,
            params: Optional[dict] = None,
            timeout: Optional[Union[int, float]] = 10,
            files: Optional[Union[dict, list]] = None,
            json: Optional[Union[dict, BaseModel]] = None,
            method: str = 'get',
    ) -> requests.Response:
        response = requests.request(
            url=url,
            method=method,
            headers=headers if headers else self.headers,
            params=params if params else self.params,
            data=data,
            files=files if files else self.files,
            json=json,
            verify=False,
            timeout=timeout
        )

        for attr in [self.data, self.json, self.files, self.params]:
            attr.clear()

        return response
