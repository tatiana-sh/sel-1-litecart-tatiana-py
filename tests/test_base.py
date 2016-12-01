import pytest
from selenium import webdriver


class TestBase:
    @pytest.fixture
    def driver(self, request):
        wd = webdriver.Chrome()
        wd.implicitly_wait(2)

        request.addfinalizer(wd.quit)
        request.cls.driver = wd
