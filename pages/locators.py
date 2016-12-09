from selenium.webdriver.common.by import By


class AdminLoginPageLocators(object):
    BASE_URL = "http://localhost/litecart/admin/login.php"
    USERNAME_INPUT = (By.NAME, 'username')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.NAME, 'login')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "[title='Logout']")


class AdminPageLocators(object):
    BASE_URL_COUNTRIES = "http://localhost/litecart/admin/?app=countries&doc=countries"
    BASE_URL_GEOZONES = "http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones"
    NAVIGATION_MENU_ITEM = (By.CSS_SELECTOR, "#box-apps-menu #app-")
    NAVIGATION_MENU_ITEM_SUBNODE = (By.CSS_SELECTOR, "#box-apps-menu #app- li")
    CONTENT_PAGE_HEADING = (By.CSS_SELECTOR, "h1")
    LOCALE_TEXT = (By.CSS_SELECTOR, ".dataTable a[href*='doc=edit']:first-child:not([title])")
    LOCALE_ZONE = (By.XPATH, "//td[a[contains(@href,'doc=edit')]]/following-sibling::td[1]")
    LOCALE_EDIT_BUTTON = (By.CSS_SELECTOR, "[name='countries_form'] a[title]")
    ZONE_TEXT_GEOZONES = (By.CSS_SELECTOR, "[name*='zone_code'] > [selected]")
    ZONE_TEXT_COUNTRIES = (By.CSS_SELECTOR, "[name*='zone_code'] > [selected]")


class MainPageLocators(object):
    BASE_URL = "http://localhost/litecart/en/"
    PRODUCT = (By.CSS_SELECTOR, ".product")
    PRODUCT_STICKER = (By.CSS_SELECTOR, ".sticker")
    NAVIGATION_MENU_ITEM = (By.CSS_SELECTOR, "#box-category-tree .content > ul > li > a")
    NAVIGATION_MENU_ITEM_SUBNODE = (By.CSS_SELECTOR, "#box-category-tree .content > ul > li li > a")
