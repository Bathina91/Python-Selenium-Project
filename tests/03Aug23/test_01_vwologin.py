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

    # input - element has following attributes
    # type = "email"
    # class ="text-input W(100%)"
    # name="username"
    # id="login-username"
    # In Selenium - we can find the elements with the inbuilt methods  ->
    # find element by_id : finds an element by its name attribute.
    # find element by_name : finds an element by its unique id attribute.
    # find element by_link_text : finds an anchor element (a) by its visible text.
    # find element by_partial_link_text : finds an anchor element (a) by a partial match of the visible text.
    # find element by_tag_name : finds an element by its HTML tag name attribute.
    # we need to import - > from selenium.webdriver.common.by import By

    email_address_ele = driver.find_element(By.ID, "login-username")
    password_ele = driver.find_element(By.NAME, "password")
    sign_in_button_ele = driver.find_element(By.ID, "js-login-btn")

    # sending the data email and password and clicking on the button
    # we have sendkeys and click()

    email_address_ele.send_keys("harish.battina@gmail.com")
    password_ele.send_keys("Hari@123")
    sign_in_button_ele.click()

    # There is a delay for 2-3 seconds

    time.sleep(10)

    assert "Dashboard" in driver.title
    driver.refresh()
    driver.get("https://sdet.live")
    driver.back()
    driver.forward()




