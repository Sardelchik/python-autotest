from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()


class TestExample:
    def test_find_elements(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://the-internet.herokuapp.com/login")
        driver.find_elements_by_name('username') # [name="username"] or //*[@name="username"]
        driver.find_elements_by_id('username') # [id="username"] or #username or //*[@id="username"]       
        driver.find_elements_by_class_name('subheader') # [class="subheader"] or .subheader or //*[@class="subheader"]
        
        
        driver.find_element(By.ID, 'username')
        pass