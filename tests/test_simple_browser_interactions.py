import pytest
from selenium import webdriver


class TestSelenium:
    @pytest.fixture
    def driver(self, request):
        wd = webdriver.Chrome()
        request.addfinalizer(wd.quit)
        return wd

    def test_open_close_browser(self, driver):
        driver.get("http://google.com")
        assert True
