import pytest
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def set_up_browser():
    driver = Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()