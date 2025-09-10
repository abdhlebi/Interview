import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    user_name = driver.find_element(By.XPATH, '//*[@id="username"]')
    user_name.send_keys("student")

    password = driver.find_element(By.XPATH, '//*[@id="password"]')
    password.send_keys("Password123")

    goo = driver.find_element(By.XPATH, '//*[@id="submit"]')
    goo.click()

    assert "successfully" in driver.title.lower(), "successfully' to be in the page title"



