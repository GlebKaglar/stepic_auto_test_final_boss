# pytest -v --tb=line --language=en test_main_page.py
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):  # Проверяем наличие ссылки, ведущей на логин
    print('Тест первый: Проверка наличия ссылки на Login Page')
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page(browser):

    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = MainPage(browser, link)
    print('Тест второй: Проверка перехода на Login Page')
    page.open()              # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина

    # инициализируем Page Object для Login Page,передаем драйвер и текущий url
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

