from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Pages.base_page import BasePage
from locators.locators import GroceryLocationsLocators


class GroceryLocations(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to(self):
        self.driver.get("https://www.amazon.com/aplf/list")

    def enter_postal_code(self, postal_code):
        """ Enters the given postal code into the postal code search """
        self.enter_text(GroceryLocationsLocators.postal_code_input, postal_code + Keys.ENTER)

    def get_locations(self):
        """ Gets the current list of grocery locations nearby """
        store_names = []
        locations = self.driver.find_elements(By.CSS_SELECTOR, "#aplf-list-container>span")
        for location in locations:
            location_name = location.find_element(By.CSS_SELECTOR, ".a-row:nth-child(1) .a-row:nth-child(1)").text
            store_names.append(location_name)
        return store_names
