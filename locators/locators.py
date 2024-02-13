from selenium.webdriver.common.by import By


class HomePageLocators:
    search_box = (By.ID, 'twotabsearchtextbox')


class GroceryLocationsLocators:
    postal_code_input = (By.ID, "postalCode")

class SearchResultsLocators:
    search_result_item = (By.CSS_SELECTOR, "[data-asin]")
