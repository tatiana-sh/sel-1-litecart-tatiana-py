from pages.locators import AdminLoginPageLocators
from tests.test_base import TestBase


class TestLitecartAdminLogin(TestBase):

    def test_admin_should_be_able_to_login_successfully(self, driver):
        self.driver.get(AdminLoginPageLocators.BASE_URL)

        username_input = self.driver.find_element(*AdminLoginPageLocators.USERNAME_INPUT)
        password_input = self.driver.find_element(*AdminLoginPageLocators.PASSWORD_INPUT)
        login_btn = self.driver.find_element(*AdminLoginPageLocators.LOGIN_BUTTON)

        username_input.send_keys("admin")
        password_input.send_keys("admin")
        login_btn.click()

        logout_btn = self.driver.find_element(*AdminLoginPageLocators.LOGOUT_BUTTON)

        assert logout_btn.is_displayed()
