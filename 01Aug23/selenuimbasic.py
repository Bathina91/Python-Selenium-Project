# call the Selenium
# use the Selenium commands

# Selenium code(python, java etc) --> API Http Request -> Chrome Drive -> Chrome Browser

from selenium import webdriver
import pytest
# Create the Session
# Send the Commands - navigate to an url

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
# return driver value will be stored permanently, extra variable whereas yield is for better
# memory management
# VWO - Application

def test_open_url_verify_title(driver):
    driver.get("https://app.vwo.com")
    print("driver.title")
    assert "Login - VWO" == driver.title
