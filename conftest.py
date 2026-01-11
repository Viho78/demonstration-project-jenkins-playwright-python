import pytest
import requests
import secret # file containing @username= and @password= variables
import os 
import pymssql

#--------------------------for UI tests--------------------------
@pytest.fixture
def title_text():
    yield "Restful-booker-platform demo"

#--------------------------for API tests--------------------------
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

#--------------------------for backend SQL tests--------------------------
@pytest.fixture
def get_new_DB_conn():
    url = "https://restful-booker.herokuapp.com/auth"
    #for running backend SQL tests tests locally without setting env variables
    if 'username' not in os.environ or 'password' not in os.environ:   
        conn = pymssql.connect(
            host='some_server_new', 
            user=secret.username, 
            password=secret.password, 
            database='example_hotel_db_new'
        )
    else: #for running backend SQL tests via Jenkins where credentials are set as env variables
        conn = pymssql.connect(
            host='some_server_new', 
            user=os.environ['username'], 
            password=os.environ['password'], 
            database='example_hotel_db_new'
        )
    cursor = conn.cursor(as_dict=True)
    print("SQL Connection established")
    yield cursor, conn
    cursor.close()
    conn.close()
    print("SQL Connection closed")

@pytest.fixture
def get_legacy_DB_conn():
    url = "https://restful-booker.herokuapp.com/auth"
    #for running backend SQL tests tests locally without setting env variables
    if 'username' not in os.environ or 'password' not in os.environ:   
        conn = pymssql.connect(
            host='some_server_legacy', 
            user=secret.username, 
            password=secret.password, 
            database='example_hotel_db_legacy'
        )
    else: #for running backend SQL tests via Jenkins where credentials are set as env variables
        conn = pymssql.connect(
            host='some_server_legacy', 
            user=os.environ['username'], 
            password=os.environ['password'], 
            database='example_hotel_db_legacy'
        )
    cursor = conn.cursor(as_dict=True)
    print("SQL Connection established")
    yield cursor, conn
    cursor.close()
    conn.close()
    print("SQL Connection closed")

#--------------------------for UI tests with Playwright--------------------------
# This should be commented, used only to run tests locally with arguments like headless etc. 
# When runned from command line it will forece running only with firefox browser
#@pytest.fixture(scope="session")
#def browser(playwright):
#    browser = playwright.firefox.launch(headless=False, timeout=10000)
#    yield browser
#    browser.close()

