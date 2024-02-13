from selenium.webdriver.common.keys import Keys

from Pages.base_page import BasePage
from locators.locators import HomePageLocators


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to(self):
        """ Navigates to Amazon home page """
        self.driver.get("https://www.amazon.com")

    def search_for(self, search_text):
        """ Searches for the given string in the Amazon search """
        self.enter_text(HomePageLocators.search_box, search_text + Keys.RETURN)
