import re
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestClass:
    @allure.feature('Поиск задач на GitHub')
    @allure.story('Поиск по заголовкам задач')
    def test_function1(self, set_up_browser):
        with allure.step('Открыть страницу задач проекта VSCode на GitHub'):
            driver = set_up_browser
            driver.get("https://github.com/microsoft/vscode/issues")

        with allure.step('Найти поле поиска и ввести запрос'):
            elem_id = driver.find_element(By.ID, 'js-issues-search')
            elem_id.clear()
            elem_id.click()
            elem_id.send_keys('in:title ')
            elem_id.send_keys('bug' + Keys.ENTER)

        with allure.step('Ожидание результатов поиска'):
            wait = WebDriverWait(driver, 10)  # Указываем максимальное время ожидания в секундах
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="js-navigation-container js-active-navigation-container"]')))

        with allure.step('Проверка результатов поиска'):
            issues = driver.find_elements(By.CSS_SELECTOR, 'div[class="js-navigation-container js-active-navigation-container"]')
            for issue in issues:
                assert "bug" in issue.text.lower(), f"Задача {issue.text} не содержит слово 'bug'"

    
    @allure.feature('Тестирование GitHub Issues')
    @allure.story('Поиск issues по автору')
    def test_function2(self, set_up_browser):
        with allure.step('Открыть страницу issues проекта VSCode'):
            driver = set_up_browser
            driver.get("https://github.com/microsoft/vscode/issues")

        with allure.step('Кликнуть на выпадающий список авторов'):
            elem_xpath1 = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*/summary[@title="Author"]'))
            )
            elem_xpath1.click()

        with allure.step('Ввести имя автора и применить фильтр'):
            elem_id1 = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'author-filter-field'))
            )
            elem_id1.click()
            elem_id1.send_keys('bpasero')

            elem_xpath2 = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@name="author"]'))
            )
            elem_xpath2.click()

        with allure.step('Проверить, что фильтр применился корректно'):
            search_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[id="js-issues-search"]'))
            )
            assert 'bpasero' in search_field.get_attribute('value')


    @allure.feature('Тестирование поиска на GitHub')
    @allure.story('Поиск репозиториев по количеству звёзд')
    def test_function3(self, set_up_browser):
        with allure.step('Открыть страницу расширенного поиска GitHub'):
            driver = set_up_browser
            driver.get("https://github.com/search/advanced")

        with allure.step('Выбрать язык программирования Python'):
            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.ID, 'search_language'))).click()
            python_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//select[@id="search_language"]/optgroup[@label="Popular"]/option[@value="Python"]')))
            python_option.click()

        with allure.step('Ввести количество звёзд более 20000'):
            stars_input = wait.until(EC.element_to_be_clickable((By.ID, 'search_stars')))
            stars_input.send_keys('>20000')

        with allure.step('Ввести имя файла environment.yml'):
            filename_input = wait.until(EC.element_to_be_clickable((By.ID, 'search_filename')))
            filename_input.send_keys('environment.yml')

        with allure.step('Нажать кнопку поиска'):
            search_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*/div[@class="d-flex d-md-block"]/button[contains(text(),"Search")]')))
            search_button.click()

        with allure.step('Проверить количество звёзд у репозиториев'):
            boxes = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[class="Box-sc-g0xbh4-0 hDWxXB"]')))
            for box in boxes:
                stars_text = box.find_element(By.CSS_SELECTOR, 'span[class="Text-sc-17v1xeu-0 gPDEWA"]').text
                stars_text = re.sub(r'[^0-9,]', '', stars_text)
                if stars_text.isdigit():
                    stars_count = int(stars_text.replace('k', '').replace(',', '')) * 1000
                    assert stars_count > 20000, f"Репозиторий {box.text} имеет количество звёзд меньше 20000"
                else:
                    print(f"Не удалось преобразовать '{stars_text}' в число.")


    @allure.feature('Тестирование веб-сайта Skillbox')
    @allure.story('Проверка функциональности выбора курсов')
    def test_function4(self, set_up_browser):
        with allure.step('Инициализация драйвера и открытие страницы'):
            driver = set_up_browser
            driver.maximize_window()
            driver.get("https://skillbox.ru/code/")

        with allure.step('Выбор радиобаттона "Профессия"'):
            profession_radio = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*/label[@value="profession"]'))
            )
            profession_radio.click()

        with allure.step('Изменение диапазона длительности курса'):
            duration_slider_start = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@aria-valuetext="1"]/button[@aria-label="Изменить диапозон"]'))
            )
            duration_slider_end = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@aria-valuetext="24"]/button[@aria-label="Изменить диапозон"]'))
            )

            action_chains = ActionChains(driver)
            action_chains.click_and_hold(duration_slider_start).move_by_offset(xoffset=70, yoffset=0).release().perform()
            action_chains.click_and_hold(duration_slider_end).move_by_offset(xoffset=-70, yoffset=0).release().perform()

        with allure.step('Выбор тематики курса'):
            topic_checkbox = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'ul.filter-checkboxes-list.filter-checkboxes__list li:nth-of-type(1)'))
            )
            topic_checkbox.click()

        with allure.step('Проверка наличия курса "1С-разработчик" на странице'):
            courses_elements = driver.find_elements(By.CSS_SELECTOR, 'section[class="courses-block courses-section__block"]')
            assert any("1С-разработчик" in element.text for element in courses_elements), "Курс '1С-разработчик' не найден на странице"


    @allure.feature('Тестирование графика активности коммитов на GitHub')
    @allure.story('Проверка тултипов на графике')
    def test_function5(self, set_up_browser):
        with allure.step('Инициализация драйвера и открытие страницы'):
            driver = set_up_browser
            driver.maximize_window()
            driver.get("https://github.com/microsoft/vscode/graphs/commit-activity")

        with allure.step('Наведение курсора на элемент графика и проверка тултипа'):
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'svg.viz'))
            )
            
            graph_element = driver.find_element(By.CSS_SELECTOR, 'svg.viz>g>g:nth-of-type(10)')
            ActionChains(driver).move_to_element(graph_element).perform()
            
            tooltip = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="svg-tip n"]'))
            )
            
            tooltip_text = tooltip.get_attribute('textContent')
            expected_text = '228 commits the week of Sep 10'
            assert tooltip_text == expected_text, f"Текст тултипа '{tooltip_text}' не соответствует ожидаемому '{expected_text}'"