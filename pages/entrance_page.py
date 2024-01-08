# example for code to...
import allure
# import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Entrance(BasePage):  # inherits from BasePage

    # pageFactory = reusable located elements (in a tuple format)
    USERNAME = (By.ID, "user-name")  # see implementations below!
    PASSWORD = (By.ID, "password")  # see implementations below v
    ERROR_MSG = (By.CSS_SELECTOR, ".error-message-container h3")
    SUBMIT_BTN = (By.CSS_SELECTOR, ".submit-button")

    def __init__(self, driver):
        # self.driver: WebDriver = driver  # before adding BasePage
        super().__init__(driver)  # passing the driver to super BP!

    @allure.step("Login with user: {username}  & pass: {password}")  # ToDo: delete Comments!
    def do_login(self, username, password):
        # self.driver.find_element(By.ID, "user-name").send_keys(username)  # no pageFactory!
        self.fill_text(self.USERNAME, username)  # NOTE: this is with BasePage & pageFactory!
        # self.driver.find_element(By.ID, "password").send_keys(password)  # orig
        # after adding BasePage + PageFactory, we can use its own wrapped methods
        self.fill_text(self.PASSWORD, password)  # NOTE: used with BasePage DON'T need *self!
        # self.driver.find_element(*self.SUBMIT_BTN).click()  # NOTE: used local needs *self!
        self.click(self.SUBMIT_BTN)
        # time.sleep(1)

    @allure.step("Getting the Error-Message")
    def get_errorMsg(self):
        return self.get_text(self.ERROR_MSG)  # NOTE: is used via BasePage, DON'T need *self!
