from playwright.sync_api import Page, expect
import pytest
import allure

#url for training site to practice web ui test automation
#page is about booking platform for the hotel
page_url = r'https://automationintesting.online/'

@allure.suite("SMOKE TESTS")
@allure.story("Item 105001")
@allure.label("owner", "JStanczyk")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.smoke
def test_page_opens(page: Page):
    page.goto(page_url)

    # Expect a title to be equal
    expect(page).to_have_title("Restful-booker-platform demo")
    # Expects page to have a div with the name of the hotel.
    expect(page.locator("#root-container")).to_contain_text("Shady Meadows B&B")

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
