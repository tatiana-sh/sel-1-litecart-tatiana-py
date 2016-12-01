import pytest
from selenium import webdriver


class TestLitecartProductListView:
    @pytest.fixture
    def driver(self, request):
        wd = webdriver.Chrome()
        wd.implicitly_wait(3)

        request.addfinalizer(wd.quit)
        request.cls.driver = wd

    @pytest.fixture()
    def opened_product_list_view(self, request, driver):
        request.cls.driver.get("http://localhost/litecart/en/")

    def test_each_product_in_list_should_have_no_more_stickers_than_allowed(self, opened_product_list_view):
        second_stickers_list = self.driver.find_elements_by_css_selector(".product .sticker:nth-of-type(2)")
        assert len(second_stickers_list) == 0

        categories_list_count = len(
            self.driver.find_elements_by_css_selector("#box-category-tree .content > ul > li > a"))
        for i in range(0, categories_list_count):
            self.driver.find_elements_by_css_selector("#box-category-tree .content > ul > li > a")[i].click()

            second_stickers_list = self.driver.find_elements_by_css_selector(".product .sticker:nth-of-type(2)")
            assert len(second_stickers_list) == 0

            subcategories_list_count = len(
                self.driver.find_elements_by_css_selector("#box-category-tree .content > ul > li li > a"))
            for j in range(0, subcategories_list_count):
                self.driver.find_elements_by_css_selector("#box-category-tree .content > ul > li li > a")[j].click()

                second_stickers_list = self.driver.find_elements_by_css_selector(".product .sticker:nth-of-type(2)")
                assert len(second_stickers_list) == 0
