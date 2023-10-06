# Open the browser
# Navigate to a URL
# Find the Email element and put email id = "abc@gmail.com"
# Find the Password element and put password id = "123"
# Click the button - > Sign in
import time

# Verify that the dashboard is loaded - > PyTest
# Create a report to send to QA lead - HTML - Allure report

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_vwo_login():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://app.vwo.com")

    # find element by_link_text : finds an anchor element (a) by its visible text.
    # find element by_partial_link_text : finds an anchor element (a) by a partial match of the visible text.

    # <a
    # href="https://vwo.com/free-trial/?utm_medium=website&amp;utm_source=login-page&amp;utm_campaign=mof_eg_loginpage"
    # class="text-link"
    # data-qa="bericafeqo">
    # Start a free trial
    # </a>

    # ID = "id"
    # XPATH = "xpath"
    # LINK_TEXT = "link text"
    # PARTIAL_LINK_TEXT = "partial link text"
    # NAME = "name"
    # TAG_NAME = "tag name"
    # CLASS_NAME = "class name"
    # CSS_SELECTOR = "css selector"

    # ID, NAME, CLASS NAME, LINK, Partial, css selector, xpath
    # css selector  > xpath - True / False
    # Which OS, Browser -> 2 GB RAM, now day 8 GM,
    # CSS Selector, Xpath is very small.
    # Use which ever you are comfortable.

    #link = driver.find_element(By.LINK_TEXT, "Start a free trial")
    link = driver.find_element(By.PARTIAL_LINK_TEXT, "free trial")
    link.click()
