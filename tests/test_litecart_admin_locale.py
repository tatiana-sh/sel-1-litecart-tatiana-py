import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators import AdminPageLocators
from tests.test_base_admin import TestBaseAdmin


def there_is_window_other_than(driver, old_windows, timeout=10):
    WebDriverWait(driver, timeout).until(
        lambda driver: len(old_windows) != len(driver.window_handles))
    return driver.window_handles[1]


class TestAdminLocale(TestBaseAdmin):

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

    @pytest.mark.parametrize("base_url,edit_button,zone_text", [
        (AdminPageLocators.COUNTRIES_BASE_URL, AdminPageLocators.COUNTRIES_LOCALE_EDIT_BUTTON,
         AdminPageLocators.COUNTRIES_ZONE_TEXT),
        (AdminPageLocators.GEOZONES_BASE_URL, AdminPageLocators.GEOZONES_LOCALE_EDIT_BUTTON,
         AdminPageLocators.GEOZONES_ZONE_TEXT)
    ])
    def test_admin_should_see_alpha_order_for_locale_zones(self, base_url, edit_button, zone_text, logged_in_admin):
        self.driver.get(base_url)
        ## get a number of elements with locale texts
        locale_count = len(self.driver.find_elements(*AdminPageLocators.LOCALE_ZONE_NOT_NULL))
        for i in range(0, locale_count - 1):
            ## go to zone list
            locale_zone_with_text = self.driver.find_elements(*edit_button)[i]
            locale_zone_with_text.click()
            ## extract texts from element list
            zone_element_list = self.driver.find_elements(*zone_text)
            zone_text_list = list(map((lambda x: x.text), zone_element_list))

            assert zone_text_list == sorted(zone_text_list)
            ## go back to continue the check
            self.driver.get(base_url)

    def test_reference_links_should_lead_to_new_windows(self, logged_in_admin):
        self.driver.get(AdminPageLocators.COUNTRIES_BASE_URL)

        locale_zone_with_text = self.driver.find_elements(*AdminPageLocators.COUNTRIES_LOCALE_EDIT_BUTTON)[0]
        locale_zone_with_text.click()

        external_link_count = len(self.driver.find_elements(*AdminPageLocators.COUNTRIES_EXTERNAL_LINK))

        for i in range(0, external_link_count - 1):
            main_window = self.driver.current_window_handle
            old_windows = self.driver.window_handles

            external_link = self.driver.find_elements(*AdminPageLocators.COUNTRIES_EXTERNAL_LINK)[i]
            external_link.click()

            new_window = there_is_window_other_than(self.driver, old_windows)
            self.driver.switch_to_window(new_window)

            assert new_window != main_window

            self.driver.close()
            self.driver.switch_to_window(main_window)
