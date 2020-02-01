from .pages.product_page import ProductPage
import pytest
##import time

#product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]
pytest_params = [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason='')) for i in range(10)]


#@pytest.mark.parametrize('link', urls)
#def test_guest_can_add_product_to_basket(browser, link):
@pytest.mark.parametrize('promo_offer', pytest_params)
def test_guest_can_add_product_to_basket(browser, promo_offer):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.message_after_adding_product_to_basket_should_contain_product_name(page.get_product_name())
    page.message_after_adding_product_to_basket_should_contain_product_price(page.get_product_price())
    ##time.sleep(2500)
