from selenium.webdriver.common.by import By
from pages.basepage import BasePage


from pages.basepage import BasePage


class HomePage(BasePage):

    language = (By.XPATH, '//span[text()="English"]')
    from_station = (By.XPATH, '(//select[contains(@class,"fare-selects")])[1]')
    to_station = (By.XPATH,'(//select[contains(@class,"fare-selects")])[2]')

    def language_click(self):
        self.click(self.language)

    def select_from_station(self, station):
        self.select_by_visible_text(self.from_station, station)

    def select_to_station(self, station):
        self.select_by_visible_text(self.to_station, station)
