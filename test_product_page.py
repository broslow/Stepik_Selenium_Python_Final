from .pages.product_page import ProductPage
#import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.message_after_adding_product_to_basket_should_contain_product_name(page.get_product_name())
    page.message_after_adding_product_to_basket_should_contain_product_price(page.get_product_price())
    #time.sleep(2500)
