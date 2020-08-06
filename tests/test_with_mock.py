from time import sleep

import pytest
import requests
from selenium.webdriver import Chrome, ChromeOptions


@pytest.fixture()
def driver():
    options = ChromeOptions()
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--allow-insecure-localhost')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--proxy-server=http://localhost:1080")
    driver = Chrome(options=options, executable_path='../driver/chromedriver')
    yield driver
    driver.quit()


def test_hello_mock(driver):
    requests.put("http://localhost:1080/mockserver/expectation", json={
        "httpRequest": {
            "path": "/"
        },
        "httpResponse": {
            "body": "Hello from Mock!"
        }
    })

    # Откуда app?
    driver.get('http://app:8080')
    sleep(10)


def test_mock_book(driver):
    requests.put("http://localhost:1080/mockserver/expectation", json={
        "httpRequest": {
            "path": "/books"
        },
        "httpResponse": {
            "body": {
                "type": "JSON",
                "json": "{Russel':'History of Western Philosophy'}"
            }
        }
    })

    driver.get('http://app:8080/books')
    sleep(10)


