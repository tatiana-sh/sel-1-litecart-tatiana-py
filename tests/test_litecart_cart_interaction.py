import pytest
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element, staleness_of
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators import MainPageLocators, CartPageLocators
from pages.locators import ProductPageLocators
from tests.test_base import TestBase


class TestLitecartCartInteractions(TestBase):
    @pytest.fixture()
    def opened_product_list_view(self, request, driver):
        request.cls.driver.get(MainPageLocators.BASE_URL)

    def test_cart_should_update_counter_on_add_remove_product(self, opened_product_list_view):
        wait = WebDriverWait(self.driver, 2)  # seconds
        for num in range(1, 4):
            product = \
            self.driver.find_elements(*MainPageLocators.CAMPAIGNS_SECTION)[0].find_elements(*MainPageLocators.PRODUCT)[
                0]

            product.find_elements(*MainPageLocators.PRODUCT_LINK)[0].click()

            size_dropdown = self.driver.find_elements(*ProductPageLocators.SIZE_DROPDOWN)[0]
            size_dropdown.click()
            size_dropdown.find_elements_by_css_selector("[value]")[num].click()

            add_to_cart_btn = self.driver.find_elements(*ProductPageLocators.ADD_TO_CART_BTN)[0]
            add_to_cart_btn.click()

            wait.until(text_to_be_present_in_element(CartPageLocators.CART_PRODUCT_COUNTER, str(num)))

            self.driver.get(MainPageLocators.BASE_URL)

        cart_product_counter = self.driver.find_elements(*CartPageLocators.CART_PRODUCT_COUNTER)[0]
        assert cart_product_counter.text == "3"

        checkout_cart_link = self.driver.find_elements(*CartPageLocators.CHECKOUT_LINK)[0]
        checkout_cart_link.click()

        for num in range(1, 4):
            remove_from_cart_btn = self.driver.find_elements(*CartPageLocators.REMOVE_FROM_CART_BTN)[0]
            remove_from_cart_btn.click()
            element_in_cart = self.driver.find_element(*CartPageLocators.ORDER_QUANTITY)

            wait.until(staleness_of(element_in_cart))

        self.driver.get(MainPageLocators.BASE_URL)

        cart_product_counter = self.driver.find_elements(*CartPageLocators.CART_PRODUCT_COUNTER)[0]
        assert cart_product_counter.text == "0"
