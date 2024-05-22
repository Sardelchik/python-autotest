import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



@allure.feature("Тест github")
def test_first_case(set_up_browser):
    pass


@allure.feature("Тест github")
def test_second_case(set_up_browser):
    driver = set_up_browser
    with allure.step("Открытие сайта github и поиск элементов"):
        driver.get("https://github.com/microsoft/vscode/issues")
        author_button = driver.find_element(By.XPATH, "//summary[@data-hotkey='u']")
        author_button.click()

        search_input = driver.find_element(By.XPATH, "//input[@id='author-filter-field']")
        search_input.send_keys("bpasero" + Keys.ENTER)
        button = driver.find_element(By.XPATH, "//button[@class='SelectMenu-item d-block js-new-item-value']")

    with allure.step("Нажатие найденной кнопки"):
        button.click()

        WebDriverWait(driver, 100)

        search_input = driver.find_element(By.XPATH, "//input[@id='js-issues-search']")

        assert "bpasero" in search_input.text


@allure.feature("Тест github")
def test_third_case(set_up_browser):
    pass

@allure.feature("Тест skillbox")
def test_fourth_case(set_up_browser):
    pass


@allure.feature("Тест github")
def test_fifth_case(set_up_browser):
    pass