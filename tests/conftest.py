import pytest
from selenium.webdriver import Chrome, ChromeOptions


@pytest.fixture
def driver():

    options = ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = Chrome(options=options)
    yield driver
    driver.quit()