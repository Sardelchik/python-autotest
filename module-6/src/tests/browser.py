import pytest
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def set_up_browser():
    options = Options()
    options.page_load_strategy = 'normal'
    driver = Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(3)
    yield driver
    driver.quit()