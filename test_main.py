#------------------------------------------------------------------
from playwright.sync_api import Page, expect

import pytest

import allure

#------------------------------statics------------------------------------
#url for training site to practice web ui test automation
#page is about booking platform for the hotel
page_url = r'https://automationintesting.online/'





#------------------------------tests------------------------------------
@pytest.fixture
def title_text():
    yield "Restful-booker-platform demo"


#testing if main page opens correctly
@allure.suite("SMOKE TESTS")
@allure.story("Item 105001")
@allure.label("owner", "JStanczyk")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.smoke
def test_page_opens(page: Page, title_text):
    page.goto(page_url)
    # Expect a title to be equal
    assert expect(page).to_have_title(title_text) == None
    # Expects page to have a div with the name of the hotel.
    assert expect(page.locator("#root-container")).to_contain_text("Shady Meadows B&B") == None


#testing something
@allure.suite("SMOKE TESTS")
@allure.story("Item 105001")
@allure.label("owner", "JStanczyk")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.smoke
def test_get_started_link(page: Page):
    page.goto(page_url)
    pass

if __name__ == "__main__":
    pass
