from .pages.product_page import ProductPage
import pytest
import time

#product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]
pytest_params = [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason='')) for i in range(10)]


##@pytest.mark.parametrize('link', urls)
##def test_guest_can_add_product_to_basket(browser, link):
# @pytest.mark.parametrize('promo_offer', pytest_params)
# def test_guest_can_add_product_to_basket(browser, promo_offer):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
    # link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    # page = ProductPage(browser, link)
    # page.open()
    # page.add_product_to_basket()
    # page.solve_quiz_and_get_code()
    # page.message_after_adding_product_to_basket_should_contain_product_name(page.get_product_name())
    # page.message_after_adding_product_to_basket_should_contain_product_price(page.get_product_price())

# @pytest.mark.skip # пропускаем падающий тест
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
    # page = ProductPage(browser, link)
    # page.open()
    # page.add_product_to_basket()
    # page.message_about_adding_product_to_basket_is_not_presented()

# def test_guest_cant_see_success_message(browser):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
    # page = ProductPage(browser, link)
    # page.open()
    # page.message_about_adding_product_to_basket_is_not_presented()

# @pytest.mark.skip # пропускаем падающий тест
# def test_message_disappeared_after_adding_product_to_basket(browser):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
    # page = ProductPage(browser, link)
    # page.open()
    # page.add_product_to_basket()
    # time.sleep(1)
    # page.message_about_adding_product_to_basket_is_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
