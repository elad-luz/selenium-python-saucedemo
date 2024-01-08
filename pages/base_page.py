# this will act as super to all pages
import time
from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.support.wait import WebDriverWait

class BasePage:  # NOTE: file_name (base_page) != class (BasePage)
    """ Wrapper for selenium operations """

    # constructor for getting driver
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def click(self, locator) -> None:
        # time.sleep(1)  # can add sleep if needed
        self.driver.find_element(*locator).click()

    def fill_text(self, locator, txt: str) -> None:
        el = self.driver.find_element(*locator)
        el.clear()
        # time.sleep(1)
        el.send_keys(txt)

    def get_text(self, locator) -> str:
        time.sleep(1)  # here I want to wait for text!
        return self.driver.find_element(*locator).text
