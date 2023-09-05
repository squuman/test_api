import pytest
import allure


@allure.story("Тестовый класс")
class TestExample:

    @allure.title("Тестовая функция")
    def test(self):
        assert True
