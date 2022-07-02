from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        # assert True
        substring = 'login'
        full_string = self.browser.current_url
        assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"
        print('1) Url верный')
        time.sleep(3)

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        # assert True
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not found!'
        print('2) Login form присутствует')
        time.sleep(3)

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        # assert True
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is not found!'
        print('3) Register form присутствует')
        time.sleep(3)
