import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()


class TestCharts:
    def test_tooltip(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://6uvr8r.csb.app/demo/TooltipDemo.html')
        el = driver.find_element(By.XPATH, '//button/span[contains(text(), "Save")]')
        action_chains = webdriver.ActionChains(driver)
        action_chains.move_to_element(el).perform()
        driver.find_element(By.XPATH, '//span[contains(@class, "plus")]/parent::button').click()
        driver.find_element(By.XPATH, '//span[contains(@class, "plus")]/parent::button').click()


    def test_canvas_pie(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://li6smj.csb.app/')
        action_chains = webdriver.ActionChains(driver)
        action_chains.move_to_element_with_offset(driver.find_elements(By.CSS_SELECTOR, 'canvas'), xoffset=300, yoffset=50).perform()


    def test_svg_pie(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://mo1n471m5j.csb.app/')
        action_chains = webdriver.ActionChains(driver)
        time.sleep(13)
        action_chains.move_to_element(driver.find_elements(By.CSS_SELECTOR, '.highcharts-point.highcharts-color-2'))\
            .perform()


    def test_table(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://rz7b08.csb.app/demo/DataTableDemo.html')
        driver.find_element(By.CSS_SELECTOR, '[placeholder="Keyword Search"]').send_keys('Egypt')
        driver.find_element(By.XPATH, '//td[contains(text(), "Simona")]/preceding-sibling::td/descendant::div[@role="checkbox"]').click()
        driver.find_element(By.XPATH, '//span[contains(text(), "Name")]').click()
        pass