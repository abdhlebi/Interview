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
    driver.get("https://www.youtube.com")
    time.sleep(5)  # Let the page load
    search_box = driver.find_element(By.XPATH, '//*[@id="center"]/yt-searchbox/div[1]/form/input')
    search_box.send_keys("SDET Automation Tutorial")
    search_box.submit()

    time.sleep(5)  # Wait for results

    assert "youtube" in driver.title.lower(), "Expected 'youtube' to be in the page title"

# Pytest hook for logging results
# ------------------------------
def pytest_runtest_logreport(report):
    if report.when == "call":  # after test function runs
        with open("test_results.txt", "a") as f:
            f.write(f"{report.nodeid} - {report.outcome}\n")
