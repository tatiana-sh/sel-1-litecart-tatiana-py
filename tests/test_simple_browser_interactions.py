from tests.test_base import TestBase


class TestSelenium(TestBase):
    def test_open_close_browser(self, driver):
        self.driver.get("http://google.com")

        assert True
