from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_btn.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text.strip()

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text.strip()

    def message_after_adding_product_to_basket_should_contain_product_name(self, product_name):
        product_added_to_basket_msg = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET_MSG).text.strip()
        assert product_name + " has been added to your basket" in product_added_to_basket_msg, "Incorrect message after adding product to basket (product name)"

    def message_after_adding_product_to_basket_should_contain_product_price(self, product_price):
        basket_total_price_msg = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE_MSG).text.strip()
        assert "Your basket total is now " + product_price in basket_total_price_msg, "Incorrect message after adding product to basket (product price)"

    def message_about_adding_product_to_basket_is_not_presented(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET_MSG), "Success message is presented, but should not be"

    def message_about_adding_product_to_basket_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET_MSG), "Success message must disappear, but it didn't"
