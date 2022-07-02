# pytest -vs --tb=line --language=en test_product_page.py
from .pages.product_page import ProductPage


link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'


def test_guest_acn_add_product_to_basket(browser):
    print('Тест: Проверка кнопки добавления товара в корзину')
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()

