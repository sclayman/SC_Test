import time

from selenium import webdriver

from Pages.home_page import HomePage
from Pages.search_results import SearchResults


class TestSearch:

    def test_amazon_search_and_filter(self):
        driver = webdriver.Firefox()
        home_page = HomePage(driver)
        home_page.navigate_to()
        assert "Amazon.com" in driver.title
        home_page.search_for("Dualsense")
        time.sleep(3)
        search_results = SearchResults(driver)
        search_results.filter_by_brand("PlayStation")
        time.sleep(5)
        assert search_results.get_filters() == ['PlayStation']
        driver.quit()
