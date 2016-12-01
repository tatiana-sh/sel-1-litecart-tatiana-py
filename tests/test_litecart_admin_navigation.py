import pytest

from pages.locators import AdminLoginPageLocators
from pages.locators import AdminPageLocators
from tests.test_base import TestBase


class TestLitecartAdminNavigation(TestBase):
    @pytest.fixture()
    def logged_in_admin(self, request, driver):
        request.cls.driver.get(AdminLoginPageLocators.BASE_URL)

        username_input = self.driver.find_element(*AdminLoginPageLocators.USERNAME_INPUT)
        password_input = self.driver.find_element(*AdminLoginPageLocators.PASSWORD_INPUT)
        login_btn = self.driver.find_element(*AdminLoginPageLocators.LOGIN_BUTTON)

        username_input.send_keys("admin")
        password_input.send_keys("admin")
        login_btn.click()

    def test_admin_should_be_able_to_navigate_and_see_headers_on_each_page(self, logged_in_admin):
        navigation_node_count = len(self.driver.find_elements(*AdminPageLocators.NAVIGATION_MENU_ITEM))
        for i in range(0, navigation_node_count):
            self.driver.find_elements(*AdminPageLocators.NAVIGATION_MENU_ITEM)[i].click()

            page_header = self.driver.find_element(*AdminPageLocators.CONTENT_PAGE_HEADING)
            assert page_header.is_displayed and page_header.text != ""

            navigation_subnode_count = len(self.driver.find_elements(*AdminPageLocators.NAVIGATION_MENU_ITEM_SUBNODE))
            for j in range(0, navigation_subnode_count):
                self.driver.find_elements(*AdminPageLocators.NAVIGATION_MENU_ITEM_SUBNODE)[j].click()

                page_header = self.driver.find_element(*AdminPageLocators.CONTENT_PAGE_HEADING)
                assert page_header.is_displayed and page_header.text != ""
