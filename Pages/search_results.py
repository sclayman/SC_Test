from selenium.webdriver.common.by import By

from Pages.base_page import BasePage


class SearchResults(BasePage):

    def __init(self, driver):
        super().__init__(driver)

    def filter_by_brand(self, brand_name):
        """ Clicks on the given brand name in the filters """
        self.click_element((By.CSS_SELECTOR, "#brandsRefinements li[aria-label='{}'] a".format(brand_name)))

    def get_filters(self):
        """ Gets the list of currently selected filters """
        selected_filters = []
        filters = self.driver.find_elements(By.CSS_SELECTOR, "ul.sf-selected-filters-list li")
        for item in filters:
            selected_filters.append(item.text)
        return selected_filters
