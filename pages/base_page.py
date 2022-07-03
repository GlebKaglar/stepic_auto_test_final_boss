from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
import math
import time

from selenium.webdriver.support.wait import WebDriverWait  # (Проблема с accept)
from selenium.common.exceptions import TimeoutException  # (Проблема с accept)
from selenium.webdriver.support import expected_conditions as EC    # (Проблема с accept)

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    """Добавим конструктор — метод, который вызывается,
    когда мы создаем объект. Конструктор объявляется ключевым словом __init__.
    В него в качестве параметров мы передаем экземпляр драйвера и url адрес.
    Внутри конструктора сохраняем эти данные как аттрибуты нашего класса"""

    def open(self):                 # Открываем страницу в браузере
        self.browser.get(self.url)

    # Перехватывем исключения (как искать(csc, xpath, id) что искать (строка-селектор))
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

# Решаем пример и встваляем ответ в полве ввода модального окна
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        print('Answer = ', answer)
        alert.accept()
        print('Нажали на кнопку')
        try:
            WebDriverWait(self.browser, 5).until(EC.alert_is_present())  # Добавил неявное ожидание (Проблема с accept)
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except (NoAlertPresentException, TimeoutException):  # добавил TimeoutException
            print("No second alert presented")
