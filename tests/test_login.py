from time import sleep
import pytest

from pages.home_page import HomePage

@pytest.mark.smoke
def test_homepage(driver):

    driver.get("https://www.bmrc.co.in/")

    homepage = HomePage(driver)
    sleep(2)
    homepage.language_click()
    sleep(2)
    homepage.select_from_station("Kadugodi Tree Park")
    sleep(2)
    homepage.select_to_station("Garudachar Palya")
    sleep(2)

@pytest.mark.regression
def test_homepage(driver):

    driver.get("https://www.bmrc.co.in/")

    homepage = HomePage(driver)
    sleep(2)
    homepage.language_click()
    sleep(2)
    homepage.select_from_station("Sri Sathya Sai Hospital")
    sleep(2)
    homepage.select_to_station("Madavara")
    sleep(2)
