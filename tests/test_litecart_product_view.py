import pytest

from pages.locators import MainPageLocators
from tests.test_base import TestBase


class TestLitecartProductListView(TestBase):
    @pytest.fixture()
    def opened_product_list_view(self, request, driver):
        request.cls.driver.get(MainPageLocators.BASE_URL)

    def test_product_view_should_have_old_and_new_price(self, opened_product_list_view):
        pass
