import os
import time

import pytest
from selenium.webdriver.common.keys import Keys

from pages.locators import AdminCatalogPageLocators
from pages.locators import AdminLoginPageLocators
from pages.locators import AdminProductPageLocators
from tests.test_base import TestBase


class TestAdminManageProduct(TestBase):
    @pytest.fixture()
    def logged_in_admin(self, request, driver):
        request.cls.driver.get(AdminLoginPageLocators.BASE_URL)

        username_input = self.driver.find_element(*AdminLoginPageLocators.USERNAME_INPUT)
        password_input = self.driver.find_element(*AdminLoginPageLocators.PASSWORD_INPUT)
        login_btn = self.driver.find_element(*AdminLoginPageLocators.LOGIN_BUTTON)

        username_input.send_keys("admin")
        password_input.send_keys("admin")
        login_btn.click()

    def test_admin_should_be_able_to_add_new_product_to_catalog(self, logged_in_admin):
        self.driver.get(AdminCatalogPageLocators.BASE_URL)

        add_product_btn = self.driver.find_elements(*AdminCatalogPageLocators.ADD_PRODUCT_BTN)[0]
        add_product_btn.click()

        unique_product = str(time.time())
        unique_product_name = "a" + unique_product

        enable_btn = self.driver.find_elements(*AdminProductPageLocators.ENABLE_BUTTON)[0]
        product_name_input = self.driver.find_elements(*AdminProductPageLocators.PRODUCT_NAME_INPUT)[0]
        product_code_input = self.driver.find_elements(*AdminProductPageLocators.PRODUCT_CODE_INPUT)[0]
        categories = self.driver.find_elements(*AdminProductPageLocators.CATEGORIES)
        gender_male = self.driver.find_elements(*AdminProductPageLocators.GENDER_MALE)[0]
        gender_female = self.driver.find_elements(*AdminProductPageLocators.GENDER_FEMALE)[0]
        gender_uni = self.driver.find_elements(*AdminProductPageLocators.GENDER_UNI)[0]
        quantity = self.driver.find_elements(*AdminProductPageLocators.QUANTITY)[0]
        img_upload = self.driver.find_elements(*AdminProductPageLocators.IMG_UPLOAD)[0]
        date_valid_from = self.driver.find_elements(*AdminProductPageLocators.DATE_VALID_FROM)[0]
        date_valid_to = self.driver.find_elements(*AdminProductPageLocators.DATE_VALID_TO)[0]

        enable_btn.click()
        product_name_input.send_keys(unique_product_name)
        product_code_input.send_keys(unique_product)
        categories[1].click()
        gender_male.click()
        gender_female.click()
        gender_uni.click()
        quantity.clear()
        quantity.send_keys("10")
        img_upload.send_keys(os.getcwd() + "/image.png")
        self.driver.execute_script("$('[name=date_valid_from]').val('2016-01-01');")
        self.driver.execute_script("$('[name=date_valid_to]').val('2019-01-01');")

        info_tab_link = self.driver.find_elements(*AdminProductPageLocators.INFO_TAB_LINK)[0]
        info_tab_link.click()

        manufacturer_dropdown = self.driver.find_elements(*AdminProductPageLocators.MANUFACTURER_DROPDOWN)[0]
        keywords_input = self.driver.find_elements(*AdminProductPageLocators.KEYWORDS_INPUT)[0]
        short_description_input = self.driver.find_elements(*AdminProductPageLocators.SHORT_DESCRIPTION_INPUT)[0]
        description_editor = self.driver.find_elements(*AdminProductPageLocators.DESCRIPTION_EDITOR)[0]
        head_input = self.driver.find_elements(*AdminProductPageLocators.HEAD_INPUT)[0]
        meta_input = self.driver.find_elements(*AdminProductPageLocators.META_INPUT)[0]

        manufacturer_dropdown.click()
        manufacturer_dropdown.find_elements_by_css_selector("option[value='1']")[0].click()

        keywords_input.send_keys("a")
        short_description_input.send_keys("Test")

        description_editor.find_elements_by_css_selector(".trumbowyg-viewHTML-button")[0].click()
        description_editor.find_elements_by_css_selector(".trumbowyg-textarea")[0].send_keys("<p>test</p>")

        head_input.send_keys("Test")
        meta_input.send_keys("Test")

        prices_tab_link = self.driver.find_elements(*AdminProductPageLocators.PRICES_TAB_LINK)[0]
        prices_tab_link.click()

        purchase_price_input = self.driver.find_elements(*AdminProductPageLocators.PURCHASE_PRICE_INPUT)[0]
        purchase_price_unit_dropdown = \
        self.driver.find_elements(*AdminProductPageLocators.PURCHASE_PRICE_UNIT_DROPDOWN)[0]
        price_usd_input = self.driver.find_elements(*AdminProductPageLocators.PRICE_USD_INPUT)[0]
        price_euro_input = self.driver.find_elements(*AdminProductPageLocators.PRICE_EURO_INPUT)[0]

        purchase_price_input.clear()
        purchase_price_input.send_keys(Keys.HOME + "1")
        purchase_price_unit_dropdown.click()
        purchase_price_unit_dropdown.find_elements_by_css_selector("option[value='USD']")[0].click()
        price_usd_input.send_keys(Keys.HOME + "10")
        price_euro_input.send_keys(Keys.HOME + "10")

        save_btn = self.driver.find_elements(*AdminProductPageLocators.SAVE_BUTTON)[0]
        save_btn.click()

        notice_success = self.driver.find_element(*AdminCatalogPageLocators.NOTICE_SUCCESS)

        assert notice_success.is_displayed
        assert self.driver.find_elements_by_xpath("//*[contains(text(),'" + unique_product_name + "')]")[0].is_displayed
