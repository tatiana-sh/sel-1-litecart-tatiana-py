from selenium import webdriver

from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.product_page import ProductPage


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.main_page = MainPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.product_page = ProductPage(self.driver)

    def quit(self):
        self.driver.quit()
