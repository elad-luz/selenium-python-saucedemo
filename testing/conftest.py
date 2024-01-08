# this file comes to config the Test Classes behavior...
import allure
import pytest
from selenium import webdriver  # Correct import statement

# the fixture acts as a 'before class', and is not considered as a test!
@pytest.fixture(scope="class", autouse=True)  # will run once before class start running
def testing_setup(request):  # self was replaced by request (see several lines below)
    # initialize an instance of WebDriver for Chrom (needs install -&- can change to others)
    with allure.step("General setup for Starting all test-cases: open & maximize browser"):
        driver = webdriver.Chrome()
        request.cls.driver = driver
        # maximize browser window
        driver.maximize_window()
    # navigate to a URL
    with allure.step("Browse to the entrance-page"):
        driver.get("https://www.saucedemo.com/")  # Replace with any other URL (as needed)

    # after class ends... do: teardown (close the browser)
    yield
    with allure.step("Upon Testing-ended: close browser"):
        driver.quit()
