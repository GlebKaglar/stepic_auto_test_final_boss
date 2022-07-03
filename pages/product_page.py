from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import time
import math


class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        assert add_button, 'Кнопка "Добавить в корзину" не найдена'
        add_button.click()
        print('Добавляем товар в корзину')
        time.sleep(3)




