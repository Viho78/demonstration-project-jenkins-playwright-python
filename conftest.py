import pytest
import requests

@pytest.fixture
def title_text():
    yield "Restful-booker-platform demo"

#this should be commented, used to run tests locally with arguments. When runned from command line it will forece running only with firefox browser
@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.firefox.launch(headless=False, timeout=10000)
    yield browser
    browser.close()

