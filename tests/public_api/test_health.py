import json

import allure
import pytest

from api.public_api.health import Health
from dto.public_api.schema.health_response import HealthResponse


class TestHealth:
    def test_get_health(self):
        with Health().get_health() as response:
            assert response.status_code == 200
            assert HealthResponse(**json.loads(response.text))
