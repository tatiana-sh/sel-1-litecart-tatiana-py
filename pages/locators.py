from selenium.webdriver.common.by import By


class AdminLoginPageLocators(object):
    BASE_URL = "http://localhost/litecart/admin/login.php"
    USERNAME_INPUT = (By.NAME, 'username')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.NAME, 'login')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "[title='Logout']")


class AdminPageLocators(object):
    COUNTRIES_BASE_URL = "http://localhost/litecart/admin/?app=countries&doc=countries"
    GEOZONES_BASE_URL = "http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones"
    NAVIGATION_MENU_ITEM = (By.CSS_SELECTOR, "#box-apps-menu #app-")
    NAVIGATION_MENU_ITEM_SUBNODE = (By.CSS_SELECTOR, "#box-apps-menu #app- li")
    CONTENT_PAGE_HEADING = (By.CSS_SELECTOR, "h1")
    LOCALE_TEXT = (By.CSS_SELECTOR, ".dataTable a[href*='doc=edit']:first-child:not([title])")
    LOCALE_ZONE = (By.XPATH, "//td[a[contains(@href,'doc=edit')]]/following-sibling::td[1]")
    LOCALE_ZONE_NOT_NULL = (By.XPATH, "//td[a[contains(@href,'doc=edit')]]/following-sibling::td[1][not(text()='0')]")
    COUNTRIES_LOCALE_EDIT_BUTTON = (By.CSS_SELECTOR, "[name='countries_form'] a[title]")
    GEOZONES_LOCALE_EDIT_BUTTON = (By.CSS_SELECTOR, "[name='geo_zones_form'] a[title]")
    GEOZONES_ZONE_TEXT = (By.CSS_SELECTOR, "[name*='zone_code'] > [selected]")
    COUNTRIES_ZONE_TEXT = (By.XPATH, "//*[@id='table-zones']//tr[td[a]]/td[3]")


class MainPageLocators(object):
    BASE_URL = "http://localhost/litecart/en/"
    CAMPAIGNS_SECTION = (By.CSS_SELECTOR, "#box-campaigns")
    PRODUCT = (By.CSS_SELECTOR, ".product")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".name")
    PRODUCT_REGULAR_PRICE = (By.CSS_SELECTOR, ".regular-price")
    PRODUCT_CAMPAIGN_PRICE = (By.CSS_SELECTOR, ".campaign-price")
    PRODUCT_LINK = (By.CSS_SELECTOR, ".link")
    PRODUCT_STICKER = (By.CSS_SELECTOR, ".sticker")
    NAVIGATION_MENU_ITEM = (By.CSS_SELECTOR, "#box-category-tree .content > ul > li > a")
    NAVIGATION_MENU_ITEM_SUBNODE = (By.CSS_SELECTOR, "#box-category-tree .content > ul > li li > a")


class ProductPageLocators(object):
    PRODUCT = (By.CSS_SELECTOR, "#box-product")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".title")
    PRODUCT_REGULAR_PRICE = (By.CSS_SELECTOR, ".regular-price")
    PRODUCT_CAMPAIGN_PRICE = (By.CSS_SELECTOR, ".campaign-price")


class UserLoginPageLocators(object):
    REGISTER_LINK = (By.CSS_SELECTOR, '[href*="create_account"]')
    EMAIL_INPUT = (By.NAME, 'email')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.NAME, 'login')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "[href*='logout']")


class UserRegisterPageLocators(object):
    EMAIL_INPUT = (By.NAME, 'email')
    PASSWORD_INPUT = (By.NAME, 'password')
    FIRSTNAME_INPUT = (By.NAME, 'firstname')
    LASTNAME_INPUT = (By.NAME, 'lastname')
    ADDRESS1_INPUT = (By.NAME, 'address1')
    POSTCODE_INPUT = (By.NAME, 'postcode')
    CITY_INPUT = (By.NAME, 'city')
    PHONE_INPUT = (By.NAME, 'phone')
    CONFIRM_PASSWORD_INPUT = (By.NAME, 'confirmed_password')
    REGISTER_BUTTON = (By.NAME, 'create_account')
