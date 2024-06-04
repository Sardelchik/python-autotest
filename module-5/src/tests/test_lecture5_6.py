
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import Keys, ActionChains

class TestClass:
    def test_function1(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://github.com/microsoft/vscode/issues")
        elem_id = driver.find_element(By.ID, 'js-issues-search')
        elem_id.clear()
        elem_id.click()
        elem_id.send_keys('in:title ')
        elem_id.send_keys('bug' + Keys.ENTER)
        time.sleep(5)

    def test_function2(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://github.com/microsoft/vscode/issues")
        elem_xpath1 = driver.find_element(By.XPATH, '//*/summary[@title="Author"]')
        elem_xpath1.click()
        elem_id1 = driver.find_element(By.ID, 'author-filter-field')
        elem_id1.click()
        time.sleep(2)
        elem_id1.send_keys('bpasero')
        time.sleep(2)
        elem_xpath2 = driver.find_element(By.XPATH, '//button[@name="author"]')
        elem_xpath2.click()
        time.sleep(5)

    def test_function3(self, set_up_browser):
        driver = set_up_browser
        driver.get(" https://github.com/search/advanced")
        elem = driver.find_element(By.ID, 'search_language').click()
        elem1 = driver.find_element(By.XPATH, '//select[@id="search_language"]/optgroup[@label="Popular"]/option[@value = "Python"]')
        time.sleep(1)
        elem1.click()
        elem2 = driver.find_element(By.ID, 'search_stars')
        time.sleep(1)
        elem2.send_keys('>20000')
        elem3 = driver.find_element(By.ID, 'search_filename')
        time.sleep(1)
        elem3.send_keys('environment.yml')
        time.sleep(1)
        elem4 = driver.find_element(By.XPATH, '//*/div[@class="d-flex d-md-block"]/button[contains(text(),"Search")]').click()
        time.sleep(5)

    def test_function4(self, set_up_browser):
        driver = set_up_browser
        driver.maximize_window()
        driver.get("https://skillbox.ru/code/")
        elem1 = driver.find_element(By.XPATH,'//*/label[@value="profession"]').click()
        time.sleep(1)
        elem2 = driver.find_element(By.XPATH, '//div[@aria-valuetext="1"]/button[@aria-label="Изменить диапозон"]')
        action_chains = ActionChains(driver)
        action_chains.click_and_hold(elem2).move_by_offset(xoffset=70,yoffset=0).perform()
        action_chains.release().perform()
        time.sleep(1)
        elem3 = driver.find_element(By.XPATH, '//div[@aria-valuetext="24"]/button[@aria-label="Изменить диапозон"]')
        action_chains.click_and_hold(elem3).move_by_offset(xoffset=-70, yoffset=0).perform()
        action_chains.release().perform()
        time.sleep(1)
        elem4 = driver.find_element(By.CSS_SELECTOR,'ul.filter-checkboxes-list.filter-checkboxes__list li:nth-of-type(1)').click()
        time.sleep(1)
        elem5 = driver.find_element(By.CSS_SELECTOR,'ul.filter-checkboxes-list.filter-checkboxes__list li:nth-of-type(2)').click()
        time.sleep(5)

    def test_function5(self, set_up_browser):
        driver = set_up_browser
        driver.maximize_window()
        driver.get("https://github.com/microsoft/vscode/graphs/commit-activity")
        action_chains = ActionChains(driver)
        time.sleep(10)
        elem = driver.find_element(By.CSS_SELECTOR,'svg.viz>g>g:nth-of-type(10)')
        action_chains.move_to_element(elem).perform()
        time.sleep(5)