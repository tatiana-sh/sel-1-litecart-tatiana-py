import pytest
from selenium import webdriver


class TestLitecartAdminNavigation:
    @pytest.fixture
    def driver(self, request):
        wd = webdriver.Chrome()
        wd.implicitly_wait(1)

        wd.get("http://localhost/litecart/admin/login.php")

        username_input = wd.find_element_by_name("username")
        password_input = wd.find_element_by_name("password")
        login_btn = wd.find_element_by_name("login")

        username_input.send_keys("admin")
        password_input.send_keys("admin")
        login_btn.click()

        request.addfinalizer(wd.quit)
        return wd

    def test_admin_should_be_able_to_navigate_and_see_headers_on_each_page(self, driver):
        navigation_node_count = len(driver.find_elements_by_css_selector("#box-apps-menu #app-"))
        for i in range(0, navigation_node_count):
            driver.find_elements_by_css_selector("#box-apps-menu #app-")[i].click()

            page_header = driver.find_element_by_css_selector("h1")
            assert page_header.is_displayed and page_header.text != ""

            navigation_subnode_count = len(driver.find_elements_by_css_selector("#box-apps-menu #app- li"))
            for j in range(0, navigation_subnode_count):
                driver.find_elements_by_css_selector("#box-apps-menu #app- li")[j].click()

                page_header = driver.find_element_by_css_selector("h1")
                assert page_header.is_displayed and page_header.text != ""
