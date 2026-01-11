import pytest
import requests
import secret # file containing @username= and @password= variables
import os 

@pytest.fixture
def title_text():
    yield "Restful-booker-platform demo"

@pytest.fixture
def get_API_token():
    url = "https://restful-booker.herokuapp.com/auth"
    #for running API tests locally without setting env variables
    if 'username' not in os.environ or 'password' not in os.environ:   
        payload = { 
            "username": secret.username,
            "password": secret.password
        }
    else: #for running API via Jenkins where credentials are set as env variables
        payload = {
            "username": os.environ['username'], 
            "password": os.environ['password']
        }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    token = response.json().get("token")
    yield token

# This should be commented, used only to run tests locally with arguments. 
# When runned from command line it will forece running only with firefox browser
#@pytest.fixture(scope="session")
#def browser(playwright):
#    browser = playwright.firefox.launch(headless=False, timeout=10000)
#    yield browser
#    browser.close()

