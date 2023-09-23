import allure
import json

from api.public_api.entries import Entries
from dto.public_api.schema.entries_response import EntriesResponse


@allure.title("Тестирование элементов")
class TestEntries:
    @allure.title("Получение объекта")
    def test_get_entry(self):
        with Entries().get_entries() as response:
            assert response.status_code == 200
            assert EntriesResponse(**json.loads(response.text))
