# Functions
# 1. test_scores_service - it’s purpose is to test our web service. It will get the application
# URL as an input, open a browser to that URL, select the score element in our web page,
# check that it is a number between 1 to 1000 and return a boolean value if it’s true or not.
# 2. main_function to call our tests function. The main function will return -1 as an OS exit
# code if the tests failed and 0 if they passed.

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions


def test_scores_service(app_url):
    try:
        # Chrome web driver
        driver_service = ChromeService(executable_path="/Users/gilspiegel/Downloads/chromedriver-mac-arm64-2/chromedriver")
        driver_options = ChromeOptions()
        driver_options.add_argument('--headless')  # Run the browser in headless mode
        driver = webdriver.Chrome(service=driver_service, options=driver_options)
        driver.get(app_url)

        # Wait for the page to load
        time.sleep(2)

        # Find the score element and get its text
        score_element = driver.find_element(By.ID, "score")
        score_text = score_element.text

        # Check if the score is a number between 1 and 1000
        score_valid = False
        try:
            score = int(score_text)
            if 1 <= score <= 1000:
                score_valid = True
        except ValueError:
            pass

        driver.quit()  # Close the browser

        return score_valid
    except Exception as e:
        print("An error occurred:", str(e))
        return False


def main_function():
    app_url = "http://127.0.0.1:5000/"
    test_result = test_scores_service(app_url)
    if test_result:
        print("Tests passed.")
        return 0
    else:
        print("Tests failed.")
        return -1


if __name__ == "__main__":
    exit_code = main_function()
    os._exit(exit_code)
