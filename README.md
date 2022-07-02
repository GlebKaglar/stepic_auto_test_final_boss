# stepic_auto_test_final_boss

It's a final project of auto test course on [Stepik](https://stepik.org/course/575)

**base_page.py** - методы,которые применяются по всему проекту в целом.

**locators.py** - локаторы в виде констант. Локаторы каждой отдельной страницы завёрнуты в класс, чтобы было удобно импортировать

**main_page.py / login_page.py** - методы по конкретной странице, завернутые в класс этой страницы. Класс этот - условный MainPage - наследник класса BasePage, чтобы можно было пользоваться методами, описанными в base_page.py

**test_main_page** - файл для запуска тестов.

