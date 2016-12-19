import pytest

from pages.locators import MainPageLocators
from pages.locators import ProductPageLocators
from tests.test_base import TestBase


class TestLitecartProductView(TestBase):
    @pytest.fixture()
    def opened_product_list_view(self, request, driver):
        request.cls.driver.get(MainPageLocators.BASE_URL)

    def test_product_view_should_have_matching_name_old_and_new_price(self, opened_product_list_view):
        first_product_campaigns = \
        self.driver.find_elements(*MainPageLocators.CAMPAIGNS_SECTION)[0].find_elements(*MainPageLocators.PRODUCT)[0]

        ## save values from main page
        first_product_name = first_product_campaigns.find_elements(*MainPageLocators.PRODUCT_NAME)[0].text
        first_product_regular_price = first_product_campaigns.find_elements(*MainPageLocators.PRODUCT_REGULAR_PRICE)[
            0].text
        first_product_campaign_price = first_product_campaigns.find_elements(*MainPageLocators.PRODUCT_CAMPAIGN_PRICE)[
            0].text

        ## go to product view
        first_product_campaigns.find_elements(*MainPageLocators.PRODUCT_LINK)[0].click()

        current_product_campaigns = self.driver.find_elements(*ProductPageLocators.PRODUCT)[0]

        assert first_product_name == current_product_campaigns.find_elements(*ProductPageLocators.PRODUCT_NAME)[0].text
        assert first_product_regular_price == \
               current_product_campaigns.find_elements(*ProductPageLocators.PRODUCT_REGULAR_PRICE)[0].text
        assert first_product_campaign_price == \
               current_product_campaigns.find_elements(*ProductPageLocators.PRODUCT_CAMPAIGN_PRICE)[0].text

    def test_product_view_should_have_styling_for_old_and_new_price(self, opened_product_list_view):
        first_product_campaigns = \
        self.driver.find_elements(*MainPageLocators.CAMPAIGNS_SECTION)[0].find_elements(*MainPageLocators.PRODUCT)[0]

        ## save values from main page
        first_product_regular_price_color = \
        first_product_campaigns.find_elements(*MainPageLocators.PRODUCT_REGULAR_PRICE)[0].value_of_css_property("color")
        first_product_campaign_price_color = \
        first_product_campaigns.find_elements(*MainPageLocators.PRODUCT_CAMPAIGN_PRICE)[0].value_of_css_property(
            "color")
        first_product_regular_price_style = \
        first_product_campaigns.find_elements(*MainPageLocators.PRODUCT_REGULAR_PRICE)[0].value_of_css_property(
            "text-decoration")
        first_product_campaign_price_style = \
        first_product_campaigns.find_elements(*MainPageLocators.PRODUCT_CAMPAIGN_PRICE)[0].value_of_css_property(
            "font-weight")

        ## go to product view
        first_product_campaigns.find_elements(*MainPageLocators.PRODUCT_LINK)[0].click()

        current_product_campaigns = self.driver.find_elements(*ProductPageLocators.PRODUCT)[0]

        ## save values from product page
        current_product_regular_price_color = \
        current_product_campaigns.find_elements(*ProductPageLocators.PRODUCT_REGULAR_PRICE)[0].value_of_css_property(
            "color")
        current_product_campaign_price_color = \
        current_product_campaigns.find_elements(*ProductPageLocators.PRODUCT_CAMPAIGN_PRICE)[0].value_of_css_property(
            "color")
        current_product_regular_price_style = \
        current_product_campaigns.find_elements(*ProductPageLocators.PRODUCT_REGULAR_PRICE)[0].value_of_css_property(
            "text-decoration")
        current_product_campaign_price_style = \
        current_product_campaigns.find_elements(*ProductPageLocators.PRODUCT_CAMPAIGN_PRICE)[0].value_of_css_property(
            "font-weight")

        assert "rgba(119, 119, 119, 1)" == first_product_regular_price_color
        assert "rgba(204, 0, 0, 1)" == first_product_campaign_price_color
        assert "rgba(102, 102, 102, 1)" == current_product_regular_price_color
        assert "rgba(204, 0, 0, 1)" == current_product_campaign_price_color
        assert "line-through" == first_product_regular_price_style
        assert "bold" == first_product_campaign_price_style
        assert "line-through" == current_product_regular_price_style
        assert "bold" == current_product_campaign_price_style
