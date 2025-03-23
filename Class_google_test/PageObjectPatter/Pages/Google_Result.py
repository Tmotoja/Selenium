from selenium.webdriver.common import by

class result_page:
    def __init__(self, driver):
        self.driver= driver
        self.search_result= (by.css_selector, "h3")

    def get_results(self):
        return self.driver.find_elements(*self.search_result)
