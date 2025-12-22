#------------------------------------------------------------------
from playwright.sync_api import Page, expect

import pytest

import allure

#------------------------------statics------------------------------------
#url for training site to practice web ui test automation
#page is about booking platform for the hotel
page_url = r'https://automationintesting.online/'





#------------------------------tests------------------------------------
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
    


#testing something
@allure.suite("SMOKE TESTS")
@allure.story("Item 105001")
@allure.label("owner", "JStanczyk")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.smoke
@pytest.mark.parametrize("labels", [
    "Name",
    "Email",
    "Phone",
    "Subject",
    "Message",
])
def test_contact_labels(page: Page, labels):
    page.goto(page_url)

    #verify if contact form exists
    assert expect(page.locator("#contact")).to_be_visible() == None
    #verify if contact form contains proper labels
    assert expect(page.locator('#contact')).to_contain_text(labels) == None
    
    

    



if __name__ == "__main__":
    pass
