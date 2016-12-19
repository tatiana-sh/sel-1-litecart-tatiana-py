from selenium.webdriver.support.wait import WebDriverWait

from pages.locators import MainPageLocators


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(MainPageLocators.BASE_URL)
        return self

    def click_product_in_campaign_section(self):
        product = \
        self.driver.find_elements(*MainPageLocators.CAMPAIGNS_SECTION)[0].find_elements(*MainPageLocators.PRODUCT)[0]
        product.find_elements(*MainPageLocators.PRODUCT_LINK)[0].click()
