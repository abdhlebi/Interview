import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_youtube_search(driver):
    driver.get("https://www.youtube.com/@Yanni")
    time.sleep(5)  # Let the page load




    assert "yanni" in driver.title.lower(), "Expected 'Yanni' to be in the page title"

