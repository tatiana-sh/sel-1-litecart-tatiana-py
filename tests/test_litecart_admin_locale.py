import pytest

from pages.locators import AdminLoginPageLocators
from pages.locators import AdminPageLocators
from tests.test_base import TestBase


class TestAdminLocale(TestBase):
    @pytest.fixture()
    def logged_in_admin(self, request, driver):
        request.cls.driver.get(AdminLoginPageLocators.BASE_URL)

        username_input = self.driver.find_element(*AdminLoginPageLocators.USERNAME_INPUT)
        password_input = self.driver.find_element(*AdminLoginPageLocators.PASSWORD_INPUT)
        login_btn = self.driver.find_element(*AdminLoginPageLocators.LOGIN_BUTTON)

        username_input.send_keys("admin")
        password_input.send_keys("admin")
        login_btn.click()

    @pytest.mark.parametrize("base_url", [
        (AdminPageLocators.COUNTRIES_BASE_URL),
        (AdminPageLocators.GEOZONES_BASE_URL)
    ])
    def test_admin_should_see_alpha_order_for_locale(self, base_url, logged_in_admin):
        self.driver.get(base_url)
        ## extract texts from element list
        locale_element_list = self.driver.find_elements(*AdminPageLocators.LOCALE_TEXT)
        locale_text_list = list(map((lambda x: x.text), locale_element_list))

        assert locale_text_list == sorted(locale_text_list)

    def test_admin_should_see_alpha_order_for_locale_zones_countries(self, logged_in_admin):
        self.driver.get(AdminPageLocators.COUNTRIES_BASE_URL)
        ## get a number of elements with locale texts
        locale_count = len(self.driver.find_elements(*AdminPageLocators.LOCALE_ZONE_NOT_NULL))
        for i in range(0, locale_count - 1):
            ## go to zone list
            locale_zone_with_text = self.driver.find_elements(*AdminPageLocators.COUNTRIES_LOCALE_EDIT_BUTTON)[i]
            locale_zone_with_text.click()
            ## extract texts from element list
            zone_element_list = self.driver.find_elements(*AdminPageLocators.COUNTRIES_ZONE_TEXT)
            zone_text_list = list(map((lambda x: x.text), zone_element_list))

            assert zone_text_list == sorted(zone_text_list)
            ## go back to continue the check
            self.driver.get(AdminPageLocators.COUNTRIES_BASE_URL)

    def test_admin_should_see_alpha_order_for_locale_zones_geozones(self, logged_in_admin):
        self.driver.get(AdminPageLocators.GEOZONES_BASE_URL)
        ## get a number of elements with locale texts
        locale_count = len(self.driver.find_elements(*AdminPageLocators.LOCALE_ZONE_NOT_NULL))
        for i in range(0, locale_count - 1):
            ## go to zone list
            locale_zone_with_text = self.driver.find_elements(*AdminPageLocators.GEOZONES_LOCALE_EDIT_BUTTON)[i]
            locale_zone_with_text.click()
            ## extract texts from element list
            zone_element_list = self.driver.find_elements(*AdminPageLocators.GEOZONES_ZONE_TEXT)
            zone_text_list = list(map((lambda x: x.text), zone_element_list))

            assert zone_text_list == sorted(zone_text_list)
            ## go back to continue the check
            self.driver.get(AdminPageLocators.GEOZONES_BASE_URL)
