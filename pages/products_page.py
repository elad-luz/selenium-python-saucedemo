# example for code to...
import allure
import time
from pages.base_page import BasePage

class Products(BasePage):  # inherits from BasePage

    # ToDo: add page methods...

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("get URL")  # ToDo: add assert in this level & move the get to BasePage...
    def get_pageURL(self):
        time.sleep(1)
        return self.driver.current_url

# ToDo:
# Incorporate the following (at this level or in BasePage):
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # Assuming `locator` is a tuple containing (By.<some_locator_strategy>, 'locator_value')
# locator = (By.ID, 'example_id')
#
# # Initialize WebDriverWait
# wait = WebDriverWait(driver, 10)
#
# # Use WebDriverWait with element_to_be_clickable
# element = wait.until(EC.element_to_be_clickable(locator))
#
# # Perform actions on the element
# element.click()
