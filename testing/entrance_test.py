# the only 2 Test Scenarios I implemented are:
# 1. Failed login show proper Error.
# 2. Successful login gets into App.

import allure
from allure_commons.types import Severity
from pages.entrance_page import Entrance  # NOTE the file_name != class
from pages.products_page import Products

# having allure report annotations (on class & method level)
@allure.epic("security")
@allure.feature("login")
@allure.story("As a user, I want to login after entering valid credentials & get proper Error, if needed")
@allure.severity(Severity.CRITICAL)  # class level propagate down to all (can be set 'per method' as well)
class TestEntrancePage:  # any method starting with "test", is recognised by PyTest as such:  see green |>

    # test: failed Login (with bad password) show proper failure message
    @allure.title("01. Proper Failed Login Message Presented")
    @allure.description("Logging-in with bad password show failure message: no match...")  # for reports !
    # @allure.severity(Severity.CRITICAL)
    def test_01_loginErrorMsg(self):
        # using allure step reporting action...:
        with allure.step("Login with Bad Password, gets Proper Error message"):
            # init page needed to Login & thus, all bellow...
            p0 = Entrance(self.driver)
            p0.do_login("standard_user", "secret")  # implement Fail login!
            errorMsg = p0.get_errorMsg()  # got Epic -> will use epic (lower) as expected ...
            print(errorMsg)
            expectedError = "epic sadface: Username and password do not match any user in this service"
            assert errorMsg.lower() == expectedError.lower(), "wrong errorMsg"

    # test: successful login gets into App
    @allure.title("02. Logging-in with Proper Credentials Succeeds")
    @allure.description("Logging-in with Proper Credentials, Succeeds getting to products-page")
    def test_02_loginSucceeds(self):
        # init page needed to Login & thus, all bellow...
        with allure.step("Login with Proper Credentials, Succeeds getting to products-page"):
            p0 = Entrance(self.driver)
            p0.do_login("standard_user", "secret_sauce")  # implement login

        with allure.step("Validate products-page URL"):
            # init products page for assertion on its URL...
            p1 = Products(self.driver)
            pageURL = p1.get_pageURL()
            print("page URL is: " + pageURL)
            expectedURL = "https://www.saucedemo.com/inventory.html"
            assert pageURL.lower() == expectedURL.lower(), "wrong URL"
