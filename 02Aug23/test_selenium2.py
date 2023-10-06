# Chrome -> # Chrome Options
# Chrome Options - Chrome with extensions, Window Size, Proxy, JS Disabled

from selenium import webdriver


def test_login():
    chrome_options = webdriver.ChromeOptions()
    extension_path = r"\Users\B Harish\PycharmProjects\Python-Selenium-Project\02Aug23\adblocker_extension_1_41_0_0.crx"
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--headless=new")

    #headless mode: in Chrome (without GUI), its fast, because consumes less resources
    #chrome_options.add_extension("extension_path")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://app.vwo.com")

