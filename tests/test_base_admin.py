import pytest

from pages.locators import AdminLoginPageLocators
from tests.test_base import TestBase


class TestBaseAdmin(TestBase):
    @pytest.fixture()
    def logged_in_admin(self, request, driver):
        request.cls.driver.get(AdminLoginPageLocators.BASE_URL)

        username_input = self.driver.find_element(*AdminLoginPageLocators.USERNAME_INPUT)
        password_input = self.driver.find_element(*AdminLoginPageLocators.PASSWORD_INPUT)
        login_btn = self.driver.find_element(*AdminLoginPageLocators.LOGIN_BUTTON)

        username_input.send_keys("admin")
        password_input.send_keys("admin")
        login_btn.click()
