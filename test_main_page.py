# pytest -v --tb=line --language=en test_main_page.py
from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):  # Проверяем наличие ссылке, ведущей на логин
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page(browser):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = MainPage(browser, link)
    page.open()              # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина


