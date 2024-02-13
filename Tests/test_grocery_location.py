import time

from selenium import webdriver

from Pages.grocery_locations import GroceryLocations


class TestGroceryLocation():

    def test_amazon_find_local_grocery(self):
        driver = webdriver.Firefox()
        grocery_locations = GroceryLocations(driver)
        grocery_locations.navigate_to()
        time.sleep(3)
        grocery_locations.enter_postal_code("93117")
        time.sleep(5)  # Not ideal, but need to wait for results to get fetched/populate
        assert grocery_locations.get_locations() == ["Whole Foods Market - Santa Barbara"]
        driver.quit()
