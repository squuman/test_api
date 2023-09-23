import allure
import pytest
import json

from api.public_api.categories import Categories
from dto.public_api.schema.categories_response import CategoriesResponse


class TestCategories:
    def test_get_categories(self):
        with Categories().get_categories() as response:
            assert response.status_code == 200
            assert CategoriesResponse(**json.loads(response.text))
