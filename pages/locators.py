from selenium.webdriver.common.by import By


class AdminLoginPageLocators(object):
    BASE_URL = "http://localhost/litecart/admin/login.php"
    USERNAME_INPUT = (By.NAME, 'username')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.NAME, 'login')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "[title='Logout']")


class AdminPageLocators(object):
    NAVIGATION_MENU_ITEM = (By.CSS_SELECTOR, "#box-apps-menu #app-")
    NAVIGATION_MENU_ITEM_SUBNODE = (By.CSS_SELECTOR, "#box-apps-menu #app- li")
    CONTENT_PAGE_HEADING = (By.CSS_SELECTOR, "h1")


class MainPageLocators(object):
    BASE_URL = "http://localhost/litecart/en/"
    PRODUCT = (By.CSS_SELECTOR, ".product")
    PRODUCT_STICKER = (By.CSS_SELECTOR, ".sticker")
    NAVIGATION_MENU_ITEM = (By.CSS_SELECTOR, "#box-category-tree .content > ul > li > a")
    NAVIGATION_MENU_ITEM_SUBNODE = (By.CSS_SELECTOR, "#box-category-tree .content > ul > li li > a")
