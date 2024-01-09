# selenium-python-saucedemo

This Project is using Selenium with Python, to perform UI Test Automation on SauceDemo.com website:

1. Project demonstrates My ability to code UI Automation Test-Scenarios on web-pages, using Selenium with Python.
2. I follow the Page Object Model (POM) Architecture - including:
    - Base Page
    - Page Classes
    - Data Source files
    - Test Cases

## Overview

The primary goal of this project, is to perform a DEMO on my Test-Capability, while testing simple UI Scenario (Login failure & Success).

## Project Structure

- `<ROOT>\junk` : This directory contains the classes for any pure python need.
- `<ROOT>\pages` : This directory contains the BasePage (for code-efficiency) & Pages-classes representing different pages of the website.
- `<ROOT>\testing` : This directory contains the test classes, with testing scenarios (per page functionality).
- in the future I will add tests & improve the structure by adding:
  - `<ROOT>\utilities` : directory to contain varied utilities for Running the Tests properly.
  - `<ROOT>\resources` : directory for config-params & data-sources, to use during testing.

##  Running Tests Locally

Installation, Setup and Run Test (after preparing it properly):

1. Pre-Condition - having PyCharm \ Visual-Studio-Code  (or any other alternative equivalent), Python etc.
2. Install all relevant dependencies as stated in requirements.txt  (use chocolatey install or other).
3. Clone this GIT repository to your local machine.
4. To run Python test locally, using PyCharm \ VCS:
    - RightClick on test (under: `<ROOT>\testing` e.g. entrance_test.py) -&- Click: Run -> See results in Terminal...
5. Running the Selenium tests-cases locally, using the 'Terminal' (Command-Line):
    - Open Terminal CMD on the project-root (e.g. `cd C:\<PATH>\<ROOT>`).
    - Issue command  →  `pytest --alluredir=.\testing\allure-results .\testing\entrance_test.py`
    - After running, generate the Allure results, via same Terminal issue following command  →  `allure generate C:\Users\USER\PySeSoucedemo\soucedemo_ui\testing\allure-results --clean` (will generate).
    - Afterward Open Allure report, via same Terminal issue following command  →  `allure open` (will open).


Enjoy...
Elad Luz

