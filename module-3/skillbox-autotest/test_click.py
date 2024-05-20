from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()


class TestClick:
    def test_click(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://www.selenium.dev/selenium/web/inputs.html')
        driver.find.element(By.XPATH, '//button/span[contains(text(), "Primary")]').click()


    def test_failed_click(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://www.selenium.dev/selenium/web/inputs.html')
        driver.find.element(By.XPATH, '//button').click()


    def test_double_click(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://www.selenium.dev/selenium/web/inputs.html')
        action_chains = webdriver.ActionChains(driver)
        action_chains.double_click(driver.find.element(By.XPATH, '//button/span[contains(text(), "Multiple")]').click())
        driver.find.element(By.XPATH, '//button/span[contains(text(), "Multiple")]').perform()


    def test_checkbox(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://www.selenium.dev/selenium/web/inputs.html')
        driver.find.element(By.CSS_SELECTOR, '[for="city1"]').click()
        driver.find.element(By.CSS_SELECTOR, '[for="city2"]').click()


    def test_radio_button(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://www.selenium.dev/selenium/web/inputs.html')
        driver.find.element(By.CSS_SELECTOR, '[for="A"]').click()
    

    def test_modal_window(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://www.selenium.dev/selenium/web/inputs.html')
        driver.find.element(By.XPATH, '(//button/span[contains(text(), "Confirm")])[2]').click()
        driver.find.element(By.CSS_SELECTOR, '[aria-label="Yes"]').click()

    
    def test_button_dropdown(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://www.selenium.dev/selenium/web/inputs.html')
        driver.find.element(By.CSS_SELECTOR, '[aria-owns="pr_id_2_overlay"]').click()
        driver.find.element(By.LINK_TEXT, 'Delete').click()


    def test_calendar(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://www.selenium.dev/selenium/web/inputs.html')
        driver.find.element(By.CSS_SELECTOR, '#range > input').click()
        driver.find.element(By.XPATH, '(//span[contains(text(), "18")])[2]').click()
        driver.find.element(By.XPATH, '(//span[contains(text(), "22")])[2]').click()
        pass