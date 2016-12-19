import time

import pytest

from pages.locators import MainPageLocators
from pages.locators import UserLoginPageLocators
from pages.locators import UserRegisterPageLocators
from tests.test_base import TestBase


class TestLitecartUserLogin(TestBase):
    @pytest.fixture()
    def opened_product_list_view(self, request, driver):
        request.cls.driver.get(MainPageLocators.BASE_URL)

    def test_new_user_should_be_able_to_register_and_login(self, opened_product_list_view):
        register_btn = self.driver.find_element(*UserLoginPageLocators.REGISTER_LINK)

        register_btn.click()

        email_input = self.driver.find_element(*UserRegisterPageLocators.EMAIL_INPUT)
        password_input = self.driver.find_element(*UserRegisterPageLocators.PASSWORD_INPUT)
        submit_register_btn = self.driver.find_element(*UserRegisterPageLocators.REGISTER_BUTTON)
        firstname_input = self.driver.find_element(*UserRegisterPageLocators.FIRSTNAME_INPUT)
        lastname_input = self.driver.find_element(*UserRegisterPageLocators.LASTNAME_INPUT)
        postcode_input = self.driver.find_element(*UserRegisterPageLocators.POSTCODE_INPUT)
        address1_input = self.driver.find_element(*UserRegisterPageLocators.ADDRESS1_INPUT)
        city_input = self.driver.find_element(*UserRegisterPageLocators.CITY_INPUT)
        phone_input = self.driver.find_element(*UserRegisterPageLocators.PHONE_INPUT)
        confirm_password_input = self.driver.find_element(*UserRegisterPageLocators.CONFIRM_PASSWORD_INPUT)

        unique_email = "a" + str(time.time()) + "@example.com"

        email_input.send_keys(unique_email)
        password_input.send_keys("1")
        confirm_password_input.send_keys("1")
        firstname_input.send_keys("Tester")
        lastname_input.send_keys("Test")
        postcode_input.send_keys("12345")
        address1_input.send_keys("Test str., 1")
        city_input.send_keys("Mantestercity")
        phone_input.clear()
        phone_input.send_keys("+110201234567")
        submit_register_btn.click()

        logout_btn = self.driver.find_element(*UserLoginPageLocators.LOGOUT_BUTTON)
        logout_btn.click()

        email_input = self.driver.find_element(*UserLoginPageLocators.EMAIL_INPUT)
        password_input = self.driver.find_element(*UserLoginPageLocators.PASSWORD_INPUT)
        login_btn = self.driver.find_element(*UserLoginPageLocators.LOGIN_BUTTON)

        email_input.send_keys(unique_email)
        password_input.send_keys("1")
        login_btn.click()

        logout_btn = self.driver.find_element(*UserLoginPageLocators.LOGOUT_BUTTON)
        logout_btn.click()

        email_input = self.driver.find_element(*UserLoginPageLocators.EMAIL_INPUT)
        assert email_input.is_displayed
