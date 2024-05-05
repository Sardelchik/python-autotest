from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

def test_open_website_and_check_title():
    options = ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get("https://skillbox.ru")
    assert 'Skillbox – образовательная платформа с онлайн-курсами.' == driver.title
    driver.quit()

if __name__ == '__main__':
    test_open_website_and_check_title()