import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help='Choose language: ar, ca, cs, da, de, en-gb, el, es, fi, fr, it, ko, nl, pl, pt, pt-br, ro, ru, sk, uk, zh-hans')


@pytest.fixture(scope='function')
def browser(request):
    language_selected = request.config.getoption('language')  # Получаем параметр language из командной строки
    print('\nStart Chrome browser for test...')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # убирает ненужные системные логи варнинги
    options.add_experimental_option('prefs', {'intl.accept_languages': language_selected})
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    print('\nQuit browser')
    browser.quit()
