import pytest
from selenium import webdriver


class TestLitecartAdminLogin:
    @pytest.fixture
    def driver(self, request):
        wd = webdriver.Chrome()
        wd.implicitly_wait(10)
        request.addfinalizer(wd.quit)
        return wd

    def test_admin_should_be_able_to_login_successfully(self, driver):
        driver.get("http://localhost/litecart/admin/login.php")

        username_input = driver.find_element_by_name("username")
        password_input = driver.find_element_by_name("password")
        login_btn = driver.find_element_by_name("login")

        username_input.send_keys("admin")
        password_input.send_keys("admin")
        login_btn.click()

        logout_btn = driver.find_element_by_css_selector("[title='Logout']")

        assert logout_btn.is_displayed()
