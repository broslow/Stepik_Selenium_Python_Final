from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_ADDED_TO_BASKET_MSG = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    BASKET_TOTAL_PRICE_MSG = (By.CSS_SELECTOR, "#messages > div:nth-child(3) > div > p:nth-child(1)")
    #PRODUCT_ADDED_TO_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) strong")
    #BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, "#messages > div:nth-child(3) strong")
