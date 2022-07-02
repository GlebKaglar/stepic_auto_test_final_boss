from .base_page import BasePage
from .locators import MainPageLocators
import time


class MainPage(BasePage):
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), 'Login link not found'
        # Символ * указывает, что мы передали менно пару (кортеж), который нужно распаковать
        print('Кнопка Login link не найдена')
        time.sleep(3)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        assert login_link, 'Login link not found'
        login_link.click()
        print('Переход на Login Page')
        time.sleep(3)
