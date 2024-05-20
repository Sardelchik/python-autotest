import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

class TestInput:
    def test_input(self, set_up_browser):
       driver = set_up_browser
       driver.get('https://www.selenium.dev/selenium/web/inputs.html')
       driver.find_element(By.NAME, 'email_input').clear()
       driver.find_element(By.NAME, 'email_input').send_keys('admin@localhost.dev')


    def test_clear(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://www.selenium.dev/selenium/web/inputs.html')
        el = driver.find_element(By.NAME, 'email_input').send_keys('admin@localhost.dev')
        el.clear()


    def test_copy_paste(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://www.selenium.dev/selenium/web/inputs.html')
        el = driver.find_element(By.NAME, 'email_input')
        el.send_keys('admin@localhost.dev')
        
        action_chains = webdriver.ActionChains(driver)

        action_chains.key_down(Keys.CONTROL).send_keys('a').perform()
        action_chains.key_down(Keys.CONTROL).send_keys('c').perform()
        el.clear()
        el.click()
        action_chains.key_down(Keys.CONTROL).send_keys('v').perform()


    def test_input_mask(self, set_up_browser):
       driver = set_up_browser
       driver.get('https://www.selenium.dev/selenium/web/inputs.html')
       el = driver.find_element(By.ID, 'basic')
       value = '12345678'
       for c in value:
           el.send_keys(c)
           time.sleep(0.2)


    def test_input_filter(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://www.selenium.dev/selenium/web/inputs.html')
        driver.find_element(By.NAME, 'email_input').send_keys('admin@localhost.dev')


    def test_input_tag(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://www.selenium.dev/selenium/web/inputs.html')
        driver.find_element(By.XPATH, '(//input)[3]').send_keys('skillbox' + Keys.ENTER)
        pass