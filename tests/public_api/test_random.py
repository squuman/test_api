import allure
import pytest

import json

from api.public_api.random import Random
from dto.public_api.schema.entries_response import EntriesResponse


@allure.story("Тестирование случайных элементов")
class TestRandom:
    @allure.title("Получение случайного элемента")
    def test_get_random(self):
        with Random().get_random() as response:
            assert response.status_code == 200
            assert EntriesResponse(**json.loads(response.text))
