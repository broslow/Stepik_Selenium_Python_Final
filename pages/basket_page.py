from .base_page import BasePage
from .locators import BasketLocators


class BasketPage(BasePage):
    def basket_is_empty_message_text(self):
        return self.browser.find_element(*BasketLocators.BASKET_IS_EMPTY_MSG).text.strip()

    def basket_is_empty_message_exists(self):
        assert self.is_element_present(*BasketLocators.BASKET_IS_EMPTY_MSG), "Сообщение о том, что корзина пуста, не найдено!"
        assert "Your basket is empty" in self.basket_is_empty_message_text(), "Сообщение о том, что корзина пуста, не корректно!"

    def basket_has_no_product(self):
        assert self.is_not_element_present(*BasketLocators.BASKET_ITEMS), "Ошибка, корзина не пуста!"

    def basket_has_products(self):
        assert self.is_element_present(*BasketLocators.BASKET_ITEMS), "Ошибка, корзина пуста!"
