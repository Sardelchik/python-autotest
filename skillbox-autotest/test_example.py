import allure


@allure.step('Проверка заголовка страницы')
def check_title(driver, title):
    assert title == driver.title


class TestExample:
    def test_example(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://skillbox.ru")
        check_title(driver = driver, title = 'Skillbox – образовательная платформа с онлайн-курсами.')


    def test_example_2(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://skillbox.ru")
        check_title(driver = driver, title = 'Skillbox – образовательная платформа с онлайн-курсами.')


    def test_example_3(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://skillbox.ru")
        check_title(driver = driver, title = 'Skillbox – образовательная платформа с онлайн-курсами.')

    def test_example_4(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://skillbox.ru")
        check_title(driver = driver, title = 'Skillbox – образовательная платформа с онлайн-курсами.')