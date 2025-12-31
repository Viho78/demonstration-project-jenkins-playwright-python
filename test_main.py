#------------------------------------------------------------------
from playwright.sync_api import Page, expect
import pytest
import allure
import testdata 

#------------------------------statics------------------------------------
#url for training site to practice web ui test automation
#page is about booking platform for the hotel
page_url = r'https://automationintesting.online/'
#test comment 5
#------------------------------tests------------------------------------
#testing if main page opens correctly
@allure.suite("Contact form")
@allure.story("Item 105001")
@allure.label("owner", "JStanczyk")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.smoke
def test_page_opens(page: Page, title_text):
    page.goto(page_url)
    assert expect(page).to_have_title(title_text) == None

#testing if contact form is visible
@allure.suite("Contact form")
@allure.story("Item 105001")
@allure.label("owner", "JStanczyk")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.smoke
def test_contact_form_opens(page: Page):
    page.goto(page_url)

    #verify if contact form exists
    assert expect(page.locator("#contact")).to_be_visible() == None
    #verify if contact form contains proper title
    assert expect(page.locator("#contact")).to_contain_text("Send Us a Message") == None

#contact form happy flow
@allure.suite("Contact form")
@allure.story("Item 105001")
@allure.label("owner", "JStanczyk")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.smoke
@pytest.mark.parametrize("name, email, phone, subject, description", 
                         [testdata.testdata_correct_1, 
                          testdata.testdata_correct_2_max_chars, 
                          testdata.testdata_correct_3_min_chars])
def test_contact_happy(page: Page, name, email, phone, subject, description):
    page.goto(page_url)
    
    #inserting test data into contact form
    page.get_by_test_id("ContactName").fill(name)
    page.get_by_test_id("ContactEmail").fill(email)
    page.get_by_test_id("ContactPhone").fill(phone)
    page.get_by_test_id("ContactSubject").fill(subject)
    page.get_by_test_id("ContactDescription").fill(description)
    page.get_by_role("button", name="Submit").click()

    #verifying successful submission communiates
    assert expect(page.get_by_text(f"Thanks for getting in touch {name}")).to_be_visible(timeout=10000) == None #extra time to process
    assert expect(page.get_by_text("We'll get back to you about")).to_be_visible() == None
    assert expect(page.get_by_text(f"{subject}")).to_be_visible() == None
    assert expect(page.get_by_text("as soon as possible.")).to_be_visible() == None

#contact form - errors in single field
@allure.suite("Contact form")
@allure.story("Item 105006")
@allure.label("owner", "JStanczyk")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("name, email, phone, subject, description, expected_error", 
                         [testdata.testdata_bad_name_1, 
                          testdata.testdata_bad_name_2,
                          testdata.testdata_bad_email_1,
                          testdata.testdata_bad_email_2,
                          testdata.testdata_bad_email_3,
                          testdata.testdata_bad_phone_1,
                          testdata.testdata_bad_phone_2,
                          testdata.testdata_bad_phone_3,
                          testdata.testdata_bad_subject_1,
                          testdata.testdata_bad_subject_2,
                          testdata.testdata_bad_subject_3,
                          testdata.testdata_bad_message_1,
                          testdata.testdata_bad_message_2,
                          testdata.testdata_bad_message_3])
def test_contact_error(page: Page, name, email, phone, subject, description, expected_error):
    page.goto(page_url)
    page.get_by_test_id("ContactName").fill(name)
    page.get_by_test_id("ContactEmail").fill(email)
    page.get_by_test_id("ContactPhone").fill(phone)
    page.get_by_test_id("ContactSubject").fill(subject)
    page.get_by_test_id("ContactDescription").fill(description)
    page.get_by_role("button", name="Submit").click()

    #verifying error messages for a field
    if name == "" or email == "" or phone == "" or subject == "" or description == "": #if a field empty
        assert expect(page.get_by_text(f"{expected_error}")).to_be_visible() == None
    elif email != "" and "@" not in email: #if email without @
        assert expect(page.get_by_text(f"{expected_error}")).to_be_visible() == None
    else: #if a field too long
        assert expect(page.get_by_text(f"{expected_error}")).to_be_visible() == None

    #veryfing that no success communicate is shown
    assert expect(page.get_by_text(f"Thanks for getting in touch {name}")).not_to_be_visible(timeout=10000) == None
    assert expect(page.get_by_text("We'll get back to you about")).not_to_be_visible(timeout=10000) == None
    assert expect(page.get_by_text("as soon as possible.")).not_to_be_visible(timeout=10000) == None





#contact form - multiple error messages at once
#contact form - verify that after bad data submitt attempt, it can be corrected and still submitted successfully
@allure.suite("Contact form")
@allure.story("Item 105006")
@allure.label("owner", "JStanczyk")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("name, email, phone, subject, description, expected_error_1, expected_error_2, " \
                            "expected_error_3, expected_error_4, expected_error_5, name_ok, email_ok, phone_ok, subject_ok, description_ok", 
                         [testdata.testdata_bad_multiple_1, 
                        ])
def test_contact_multiple_error(page: Page, name, email, phone, subject, description, expected_error_1, 
                              expected_error_2, expected_error_3, expected_error_4, expected_error_5, name_ok, email_ok, phone_ok, subject_ok, description_ok):
    page.goto(page_url)
    page.get_by_test_id("ContactName").fill(name)
    page.get_by_test_id("ContactEmail").fill(email)
    page.get_by_test_id("ContactPhone").fill(phone)
    page.get_by_test_id("ContactSubject").fill(subject)
    page.get_by_test_id("ContactDescription").fill(description)
    page.get_by_role("button", name="Submit").click()

    #verifying all expected error messages
    assert expect(page.get_by_text(f"{expected_error_1}")).to_be_visible() == None
    assert expect(page.get_by_text(f"{expected_error_2}")).to_be_visible() == None
    assert expect(page.get_by_text(f"{expected_error_3}")).to_be_visible() == None
    assert expect(page.get_by_text(f"{expected_error_4}")).to_be_visible() == None
    assert expect(page.get_by_text(f"{expected_error_5}")).to_be_visible() == None

    #veryfing that no success communicate is shown
    assert expect(page.get_by_text(f"Thanks for getting in touch {name}")).not_to_be_visible(timeout=10000) == None
    assert expect(page.get_by_text("We'll get back to you about")).not_to_be_visible(timeout=10000) == None
    assert expect(page.get_by_text("as soon as possible.")).not_to_be_visible(timeout=10000) == None

    #adding correct data to previously bad fields and submitting again
    page.get_by_test_id("ContactName").fill(name_ok)
    page.get_by_test_id("ContactEmail").fill(email_ok)
    page.get_by_test_id("ContactPhone").fill(phone_ok)
    page.get_by_test_id("ContactSubject").fill(subject_ok)
    page.get_by_test_id("ContactDescription").fill(description_ok)
    page.get_by_role("button", name="Submit").click()

    #verifying successful submission communiates after submitting again with correct data
    assert expect(page.get_by_text(f"Thanks for getting in touch {name_ok}")).to_be_visible(timeout=30000) == None #extra time to process
    assert expect(page.get_by_text("We'll get back to you about")).to_be_visible() == None
    assert expect(page.get_by_text(f"{subject_ok}")).to_be_visible() == None
    assert expect(page.get_by_text("as soon as possible.")).to_be_visible() == None


#contact form - sql injection text fields
@allure.suite("Contact form")
@allure.story("Item 105001")
@allure.label("owner", "JStanczyk")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("name, email, phone, subject, description, expected_error_1, expected_error_2, expected_error_3", 
                         [testdata.testdata_injection_1, 
                          testdata.testdata_injection_2])
def test_contact_injection(page: Page, name, email, phone, subject, description, expected_error_1, 
                              expected_error_2, expected_error_3):
    page.goto(page_url)
    page.get_by_test_id("ContactName").fill(name)
    page.get_by_test_id("ContactEmail").fill(email)
    page.get_by_test_id("ContactPhone").fill(phone)
    page.get_by_test_id("ContactSubject").fill(subject)
    page.get_by_test_id("ContactDescription").fill(description)
    page.get_by_role("button", name="Submit").click()

    #verifying all fields with injected data which will not pass general text validation
    if expected_error_1 != "":
        assert expect(page.get_by_text(f"{expected_error_1}")).to_be_visible() == None
        assert expect(page.get_by_text(f"{expected_error_2}")).to_be_visible() == None
        assert expect(page.get_by_text(f"{expected_error_3}")).to_be_visible() == None
    else:   #veryfing only fields where injection pass general textvalidation
        assert expect(page.get_by_text(f"Thanks for getting in touch {name}")).to_be_visible(timeout=10000) == None #extra time to process
        assert expect(page.get_by_text("We'll get back to you about")).to_be_visible() == None
        assert expect(page.get_by_text(f"{subject}")).to_be_visible() == None
        assert expect(page.get_by_text("as soon as possible.")).to_be_visible() == None

   

if __name__ == "__main__":
    pass
