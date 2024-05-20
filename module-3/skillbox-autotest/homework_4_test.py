import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()


class HomeworkTest:
    def test_case_1(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/microsoft/vscode/issues')
        driver.find_element(By.CSS_SELECTOR, '.form-control.form-control.subnav-search-input.input-contrast.width-full')\
            .click()
        driver.find_element(By.CSS_SELECTOR, '.form-control.form-control.subnav-search-input.input-contrast.width-full')\
            .send_keys('in:title:bug' + Keys.ENTER)


    def test_case_2(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/microsoft/vscode/issues')
        driver.find_element(By.XPATH, '(//summary)[4]').click()
        driver.find_element(By.XPATH, '(//*[@class="SelectMenu-input form-control js-filterable-field"])[1]').send_keys('bpasero')
        driver.find_element(By.XPATH, '(//*[@class="SelectMenu-item d-block js-new-item-value"])[1]').click()

    
    def test_case_3(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/search/advanced')
        driver.find_element(By.CSS_SELECTOR, '#search_language').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '(//option[contains(text(), "Python")])[1]').click()
        action_chains = webdriver.ActionChains(driver)
        driver.find_element(By.CSS_SELECTOR, '#search_stars')
        action_chains\
            .click()\
            .send_keys('>20000')\
            .perform()
        driver.find_element(By.CSS_SELECTOR, '#search_filename')
        action_chains\
            .click()\
            .send_keys('environment.yml')\
            .perform()
        driver.find_element(By.XPATH, '(//*[@class="btn flex-auto"])[2]').click()


    def test_case_4(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://skillbox.ru/code/')
        driver.find_element(By.XPATH, '(//*[@class="ui-radio-field__value ui-radio-field__value--small"])[1]').click()
        action_chains = webdriver.ActionChains(driver)
        el_1 = driver.find_element(By.XPATH, '(//*[@class="ui-range__dot"])[1]')
        action_chains\
            .click_and_hold(el_1)\
            .move_by_offset(xoffset=1, yoffset=0)\
            .perform()
        el_2 = driver.find_element(By.XPATH, '(//*[@class="ui-range__dot"])[2]')
        action_chains\
            .click_and_hold(el_2)\
            .move_by_offset(xoffset=-1, yoffset=0)\
            .perform()
        driver.find_element(By.XPATH, '(*//*[@class="filter-checkboxes-list__value"])[3]').click()


    def test_case_5(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/microsoft/vscode/graphs/commit-activity')
        action_chains = webdriver.ActionChains(driver)
        action_chains.move_to_element(driver.find_elements(By.CSS_SELECTOR, 'translate(392, 0)'))\
            .perform()
        pass