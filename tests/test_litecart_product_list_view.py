import pytest

from pages.locators import MainPageLocators
from tests.test_base import TestBase


class TestLitecartProductListView(TestBase):
    @pytest.fixture()
    def opened_product_list_view(self, request, driver):
        request.cls.driver.get(MainPageLocators.BASE_URL)

    def test_each_product_in_list_should_have_no_more_stickers_than_allowed(self, opened_product_list_view):
        second_stickers_list = self.driver.find_elements(*MainPageLocators.SECOND_PRODUCT_STICKER)
        assert len(second_stickers_list) == 0

        categories_list_count = len(
            self.driver.find_elements(*MainPageLocators.NAVIGATION_MENU_ITEM))
        for i in range(0, categories_list_count):
            self.driver.find_elements(*MainPageLocators.NAVIGATION_MENU_ITEM)[i].click()

            second_stickers_list = self.driver.find_elements(*MainPageLocators.SECOND_PRODUCT_STICKER)
            assert len(second_stickers_list) == 0

            subcategories_list_count = len(
                self.driver.find_elements(*MainPageLocators.NAVIGATION_MENU_ITEM_SUBNODE))
            for j in range(0, subcategories_list_count):
                self.driver.find_elements(*MainPageLocators.NAVIGATION_MENU_ITEM_SUBNODE)[j].click()

                second_stickers_list = self.driver.find_elements(*MainPageLocators.SECOND_PRODUCT_STICKER)
                assert len(second_stickers_list) == 0
