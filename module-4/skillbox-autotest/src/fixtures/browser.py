import pytest
import logging
from selenium import webdriver
from selenium. webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture()
def set_up_browser():
    logging.info('Browser has started')
    options = ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()
    logging.info('Browser has stopped')
