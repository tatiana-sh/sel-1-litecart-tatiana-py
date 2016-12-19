from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators import ProductPageLocators, CartPageLocators


class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def select_size(self, size):
        size_dropdown = self.driver.find_elements(*ProductPageLocators.SIZE_DROPDOWN)[0]
        size_dropdown.click()
        size_dropdown.find_elements(*ProductPageLocators.PRODUCT_SIZE_VALUE)[size].click()

    def add_item_to_cart(self, num):
        add_to_cart_btn = self.driver.find_elements(*ProductPageLocators.ADD_TO_CART_BTN)[0]
        add_to_cart_btn.click()

        wait = WebDriverWait(self.driver, 10)
        wait.until(text_to_be_present_in_element(CartPageLocators.CART_PRODUCT_COUNTER, str(num)))
        return self

    def add_item_of_size_to_cart(self, size):
        self.select_size(size)
        self.add_item_to_cart(size)
        return self
