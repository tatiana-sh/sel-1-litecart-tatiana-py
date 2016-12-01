import pytest

from pages.locators import MainPageLocators
from tests.test_base import TestBase


class TestLitecartProductListView(TestBase):
    @pytest.fixture()
    def opened_product_list_view(self, request, driver):
        request.cls.driver.get(MainPageLocators.BASE_URL)

    def test_each_product_in_list_should_have_no_more_stickers_than_allowed(self, opened_product_list_view):
        products_list_count = len(self.driver.find_elements(*MainPageLocators.PRODUCT))
        for i in range(0, products_list_count):
            current_product = self.driver.find_elements(*MainPageLocators.PRODUCT)[i]

            stickers_list = current_product.find_elements(*MainPageLocators.PRODUCT_STICKER)
            assert len(stickers_list) == 1
