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
    COUNTRIES_EXTERNAL_LINK = (By.XPATH, "//a[i[contains(@class,'fa-external-link')]]")


class AdminCatalogPageLocators(object):
    BASE_URL = "http://localhost/litecart/admin/?app=catalog&doc=catalog"
    ADD_PRODUCT_BTN = (By.CSS_SELECTOR, "[href*='category_id=0&app=catalog&doc=edit_product']")
    NOTICE_SUCCESS = (By.CSS_SELECTOR, ".notice.success")


class AdminProductPageLocators(object):
    ENABLE_BUTTON = (By.CSS_SELECTOR, "[name='status'][value='1']")
    PRODUCT_NAME_INPUT = (By.NAME, "name[en]")
    PRODUCT_CODE_INPUT = (By.NAME, "code")
    CATEGORIES = (By.NAME, "categories[]")
    DEFAULT_CATEGORY = (By.NAME, "default_category_id")
    GENDER_MALE = (By.CSS_SELECTOR, "[name='product_groups[]'][value='1-1']")
    GENDER_FEMALE = (By.CSS_SELECTOR, "[name='product_groups[]'][value='1-2']")
    GENDER_UNI = (By.CSS_SELECTOR, "[name='product_groups[]'][value='1-3']")
    QUANTITY = (By.NAME, "quantity")
    IMG_UPLOAD = (By.CSS_SELECTOR, "[type='file']")
    ADD_NEW_IMG_BTN = (By.CSS_SELECTOR, "#add-new-image")
    DATE_VALID_FROM = (By.NAME, "date_valid_from")
    DATE_VALID_TO = (By.NAME, "date_valid_to")
    INFO_TAB_LINK = (By.CSS_SELECTOR, "[href='#tab-information']")
    MANUFACTURER_DROPDOWN = (By.NAME, "manufacturer_id")
    SUPPLIER_DROPDOWN = (By.NAME, "supplier_id")
    KEYWORDS_INPUT = (By.NAME, "keywords")
    SHORT_DESCRIPTION_INPUT = (By.NAME, "short_description[en]")
    DESCRIPTION_EDITOR = (By.CLASS_NAME, "trumbowyg")
    HEAD_INPUT = (By.NAME, "head_title[en]")
    META_INPUT = (By.NAME, "meta_description[en]")
    PRICES_TAB_LINK = (By.CSS_SELECTOR, "[href='#tab-prices']")
    PURCHASE_PRICE_INPUT = (By.NAME, "purchase_price")
    PURCHASE_PRICE_UNIT_DROPDOWN = (By.NAME, "purchase_price_currency_code")
    TAX_CLASS_DROPDOWN = (By.NAME, "tax_class_id")
    PRICE_USD_INPUT = (By.NAME, "prices[USD]")
    PRICE_EURO_INPUT = (By.NAME, "prices[EUR]")
    SAVE_BUTTON = (By.NAME, "save")

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
    ADD_TO_CART_BTN = (By.NAME, "add_cart_product")
    SIZE_DROPDOWN = (By.NAME, "options[Size]")


class CartPageLocators(object):
    CART_PRODUCT_COUNTER = (By.CSS_SELECTOR, "#cart .quantity")
    CHECKOUT_LINK = (By.CSS_SELECTOR, "#cart [href*='checkout']")
    ORDER_QUANTITY = (By.CSS_SELECTOR, ".dataTable tr:not(.header) > td")
    REMOVE_FROM_CART_BTN = (By.NAME, "remove_cart_item")

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
