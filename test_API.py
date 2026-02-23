#------------------------------------------------------------------
import pytest
import allure
import testdata_API 
import requests

from playwright.sync_api import APIRequestContext, Playwright
from typing import Optional


@allure.suite("API Bookings")
@allure.story("Item 105099")
@allure.label("owner", "JStanczyk")
class Test_ContactFormTests():
    #url for training site to practice web API test automation
    #this is the API for booking page for a hotel demo site
    url_booking = "https://restful-booker.herokuapp.com/booking"

    @pytest.fixture
    def create_booking_fixture(self, get_API_token):
        #Creating a booking to be used in update booking test
        json_payload = {
            "firstname": "Initial",
            "lastname": "Booking",
            "totalprice": '100',
            "depositpaid": 'True',
            "bookingdates": {
                "checkin": "2026-01-01",
                "checkout": "2026-01-02"
            },
            "additionalneeds": "None"
        }
        response = requests.post(self.url_booking, json=json_payload)
        booking_id = response.json().get("bookingid")

        yield booking_id
        #Teardown - delete the created booking
        headers = {'Cookie': 'token=' + get_API_token}
        response_del = requests.put(self.url_booking + "/" + str(booking_id), json=json_payload, headers=headers)
        print("\nDELETE RESPONSE STATUS CODE:", response_del.status_code, 'FOR BOOKING ID:', booking_id)

    #------------------------------tests------------------------------------
    #GetBookings smoke test
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    def test_get_all_bookings(self):
        response = requests.get(self.url_booking)
        #veryfing response just to be 200 as smoke test
        assert response.status_code == 200


    #CreateBooking 
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds", 
                            [testdata_API.createbooking_testset_1, 
                            testdata_API.createbooking_testset_2,
                            testdata_API.createbooking_testset_3],
                            ids=["create booking test 1", "create booking test 2", "create booking test 3"])
    def test_create_booking(self,firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds):
        json_payload = {
            "firstname": firstname,
            "lastname": lastname,
            "totalprice": totalprice,
            "depositpaid": depositpaid,
            "bookingdates": {
                "checkin": checkin,
                "checkout": checkout
            },
            "additionalneeds": additionalneeds
        }
        response = requests.post(self.url_booking, json=json_payload)

        #veryfing all response data to match input data
        assert response.status_code == 200
        assert response.json().get("booking").get("firstname") == firstname
        assert response.json().get("booking").get("lastname") == lastname
        assert response.json().get("booking").get("totalprice") == totalprice
        assert response.json().get("booking").get("depositpaid") == depositpaid
        assert response.json().get("booking").get("bookingdates").get("checkin") == checkin
        assert response.json().get("booking").get("bookingdates").get("checkout") == checkout
        assert response.json().get("booking").get("additionalneeds") == additionalneeds 
        

    
    #CreateBooking 
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds", 
                            [testdata_API.updatebooking_testset_1, 
                            testdata_API.updatebooking_testset_2],
                            ids=["update booking test 1", "update booking test 2"])
    def test_update_booking(self, get_API_token, create_booking_fixture, firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds):
        booking_id = create_booking_fixture
        headers = {'Cookie': 'token=' + get_API_token}
        json_payload = {
            "firstname": firstname,
            "lastname": lastname,
            "totalprice": totalprice,
            "depositpaid": depositpaid,
            "bookingdates": {
                "checkin": checkin,
                "checkout": checkout
            },
            "additionalneeds": additionalneeds
        }
        new_url = self.url_booking + "/" + str(booking_id)
        response = requests.put(new_url, json=json_payload, headers=headers)

        #veryfing all response data to match input data
        assert response.status_code == 200
        assert response.json().get("firstname") == firstname
        assert response.json().get("lastname") == lastname
        if totalprice != '':
            assert response.json().get("totalprice") == int(totalprice)
        else: #cannot cast empty string to int, so checking for None
            assert response.json().get("totalprice") == None
        assert response.json().get("depositpaid") == bool(depositpaid)
        assert response.json().get("bookingdates").get("checkin") == checkin
        assert response.json().get("bookingdates").get("checkout") == checkout
        assert response.json().get("additionalneeds") == additionalneeds      



#its the same but using Playwright APIRequestContext instead of requests library to make API calls, just to practice using Playwright for API testing as well
class Test_ContactFormTests_PW:
    
    url_booking = r"https://restful-booker.herokuapp.com/booking"

    @pytest.fixture
    def create_booking_fixture(self, get_API_token, api_request_context: APIRequestContext):
        #Creating a booking to be used in update booking test
        json_payload = {
            "firstname": "Initial",
            "lastname": "Booking",
            "totalprice": '100',
            "depositpaid": 'True',
            "bookingdates": {
                "checkin": "2026-01-01",
                "checkout": "2026-01-02"
            },
            "additionalneeds": "None"
        }
        response = api_request_context.post(self.url_booking, data=json_payload)
        booking_id = response.json().get("bookingid")

        yield booking_id
        #Teardown - delete the created booking
        headers = {'Cookie': 'token=' + get_API_token}
        response_del = api_request_context.put(self.url_booking + "/" + str(booking_id), data=json_payload, headers=headers)
        print("\nDELETE RESPONSE STATUS CODE:", response_del.status, 'FOR BOOKING ID:', booking_id)


    #GetBookings smoke test
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    def test_get_all_bookings(self, api_request_context: APIRequestContext):
        response = api_request_context.get(self.url_booking)
        #veryfing response just to be 200 as smoke test
        assert response.status == 200

    #CreateBooking 
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds", 
                            [testdata_API.createbooking_testset_1, 
                            testdata_API.createbooking_testset_2,
                            testdata_API.createbooking_testset_3],
                            ids=["create booking test 1", "create booking test 2", "create booking test 3"])
    def test_create_booking(self,firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds, api_request_context: APIRequestContext):
        json_payload = {
            "firstname": firstname,
            "lastname": lastname,
            "totalprice": totalprice,
            "depositpaid": depositpaid,
            "bookingdates": {
                "checkin": checkin,
                "checkout": checkout
            },
            "additionalneeds": additionalneeds
        }
        response = api_request_context.post(self.url_booking, data=json_payload)

        #veryfing all response data to match input data
        assert response.status == 200
        assert response.json().get("booking").get("firstname") == firstname
        assert response.json().get("booking").get("lastname") == lastname
        assert response.json().get("booking").get("totalprice") == totalprice
        assert response.json().get("booking").get("depositpaid") == depositpaid
        assert response.json().get("booking").get("bookingdates").get("checkin") == checkin
        assert response.json().get("booking").get("bookingdates").get("checkout") == checkout
        assert response.json().get("booking").get("additionalneeds") == additionalneeds 


    #CreateBooking 
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds", 
                            [testdata_API.updatebooking_testset_1, 
                            testdata_API.updatebooking_testset_2],
                            ids=["update booking test 1", "update booking test 2"])
    def test_update_booking(self, get_API_token, create_booking_fixture, firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds, api_request_context: APIRequestContext):
        booking_id = create_booking_fixture
        headers = {'Cookie': 'token=' + get_API_token}
        json_payload = {
            "firstname": firstname,
            "lastname": lastname,
            "totalprice": totalprice,
            "depositpaid": depositpaid,
            "bookingdates": {
                "checkin": checkin,
                "checkout": checkout
            },
            "additionalneeds": additionalneeds
        }
        new_url = self.url_booking + "/" + str(booking_id)
        response = api_request_context.put(new_url, data=json_payload, headers=headers)

        #veryfing all response data to match input data
        assert response.status == 200
        assert response.json().get("firstname") == firstname
        assert response.json().get("lastname") == lastname
        if totalprice != '':
            assert response.json().get("totalprice") == int(totalprice)
        else: #cannot cast empty string to int, so checking for None
            assert response.json().get("totalprice") == None
        assert response.json().get("depositpaid") == bool(depositpaid)
        assert response.json().get("bookingdates").get("checkin") == checkin
        assert response.json().get("bookingdates").get("checkout") == checkout
        assert response.json().get("additionalneeds") == additionalneeds      


if __name__ == "__main__":
    pass