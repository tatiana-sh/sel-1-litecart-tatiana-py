import pytest
from selenium import webdriver


class TestLitecartAdminNavigation:
    @pytest.fixture
    def driver(self, request):
        wd = webdriver.Chrome()
        wd.implicitly_wait(2)

        request.addfinalizer(wd.quit)
        request.cls.driver = wd

    @pytest.fixture()
    def logged_in_admin(self, request, driver):
        request.cls.driver.get("http://localhost/litecart/admin/login.php")

        username_input = request.cls.driver.find_element_by_name("username")
        password_input = request.cls.driver.find_element_by_name("password")
        login_btn = request.cls.driver.find_element_by_name("login")

        username_input.send_keys("admin")
        password_input.send_keys("admin")
        login_btn.click()

    def test_admin_should_be_able_to_navigate_and_see_headers_on_each_page(self, logged_in_admin):
        navigation_node_count = len(self.driver.find_elements_by_css_selector("#box-apps-menu #app-"))
        for i in range(0, navigation_node_count):
            self.driver.find_elements_by_css_selector("#box-apps-menu #app-")[i].click()

            page_header = self.driver.find_element_by_css_selector("h1")
            assert page_header.is_displayed and page_header.text != ""

            navigation_subnode_count = len(self.driver.find_elements_by_css_selector("#box-apps-menu #app- li"))
            for j in range(0, navigation_subnode_count):
                self.driver.find_elements_by_css_selector("#box-apps-menu #app- li")[j].click()

                page_header = self.driver.find_element_by_css_selector("h1")
                assert page_header.is_displayed and page_header.text != ""
