import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# def katalon_appointment_negative():

@pytest.mark.negative
def test_katalon_appointment_negative():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()

    # Click on the Make Appointment
    # <a id="btn-make-appointment" href="./profile.php#login" class="btn btn-dark btn-lg">Make Appointment</a>
    link = driver.find_element(By.LINK_TEXT, "Make Appointment")
    # LINK Text - Full Match
    # Partial LINK Text - Partial Mathc
    link.click()

    username = driver.find_element(By.ID, "txt-username")
    username.send_keys("John Doe")

    password = driver.find_element(By.NAME, "password")
    password.send_keys("John Doe")

    login_button = driver.find_element(By.ID, "btn-login")

    login_button.click()

    error_message = driver.find_element(By.CSS_SELECTOR, "p.lead.text-danger")
    assert "Login failed! " in error_message.text



@pytest.mark.positive
def test_katalon_appointment():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()

    # Test case to automation - Manual Testing
    # Open - https://katalon-demo-cura.herokuapp.com/
    # Click on the Make Appointment
    # Put Username, Password and click Login
    # Select the 2 option, Radio, 2 Checkbox
    # Enter the Date and Text and Click Book Appointment
    # Verify that the Appointment Confirmation message is visible on the page.

    make_appointment_ele = driver.find_element(By.LINK_TEXT, "Make Appointment").click()
    username = driver.find_element(By.ID,"txt-username").send_keys("John Doe")
    password = driver.find_element(By.ID,"txt-password").send_keys("ThisIsNotAPassword")
    login_button = driver.find_element(By.ID, "btn-login").click()

    drop_down = Select(driver.find_element(By.ID, "combo_facility"))
    drop_down.select_by_visible_text("Hongkong CURA Healthcare Center")
    driver.find_element(By.ID, "chk_hospotal_readmission").click()
    driver.find_element(By.NAME, "programs").click()
    driver.find_element(By.ID, "txt_visit_date").send_keys("09/09/2023")
    driver.find_element(By.NAME, "comment").send_keys("I have a fever 101")
    driver.find_element(By.ID, "btn-book-appointment").click()

    heading_h2 = driver.find_element(By.TAG_NAME, "h2")
    assert "Appointment Confirmation" in heading_h2.text



