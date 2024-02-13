from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """Class to hold helper functions and other commonly used functions across pages"""

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, by):
        """ Clicks the given element """
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(by)).click()

    def enter_text(self, by, text):
        return (WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(by))
                .send_keys(text))
