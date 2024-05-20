from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()


class TestSlider:
    def test_slider(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://www.selenium.dev/selenium/web/inputs.html')
        el = driver.find_element(By.XPATH, '(//*[contains(@class="p-slider-handle"])[4]')
        action_chains = webdriver.ActionChains(driver)
        action_chains\
            .click_and_hold(el)\
            .move_by_offset(xoffset=50, yoffset=0)\
            .perform()
        action_chains.release().perform()       
    

    def test_splitter(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://www.selenium.dev/selenium/web/inputs.html')
        el = driver.find_element(By.XPATH, '(//*[@class="p-splitter-gutter-handle"])[1]')
        action_chains = webdriver.ActionChains(driver)
        action_chains\
            .click_and_hold(el)\
            .move_by_offset(xoffset=50, yoffset=0)\
            .perform()
        action_chains.release().perform()


    def test_switch(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://www.selenium.dev/selenium/web/inputs.html')
        driver.find_element(By.XPATH, '(//span)[2]').click()
        pass