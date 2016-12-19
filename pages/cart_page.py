from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators import CartPageLocators


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def verify_cart_product_counter(self, count):
        cart_product_counter = self.driver.find_element(*CartPageLocators.CART_PRODUCT_COUNTER)
        assert cart_product_counter.text == count

    def checkout_to_cart(self):
        checkout_cart_link = self.driver.find_element(*CartPageLocators.CHECKOUT_LINK)
        checkout_cart_link.click()
        return self

    def remove_from_cart(self):
        remove_from_cart_btn = self.driver.find_element(*CartPageLocators.REMOVE_FROM_CART_BTN)
        remove_from_cart_btn.click()
        element_in_cart = self.driver.find_element(*CartPageLocators.ORDER_QUANTITY)

        wait = WebDriverWait(self.driver, 10)
        wait.until(staleness_of(element_in_cart))
        return self
