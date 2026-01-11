# demonstration-project-jenkins-playwright-python
Hello!

**This is demonstration project for python automated testing with usage of playwright / jenkins / requests / pymssql / oracledb I would write for Hotel Booking page.**

**This are very simplistic scenarios to test comparing to real life cases I tested, however I think of it as a fairly quick to read and vaulable sample for recruitment processes.**

Juliusz Stańczyk


-------------------------------- General introduction ---------------------------------------------

Tests are integrated from my local machine to **Git/Jenkins** with use of **SocketXP** (it casts localhost to public address so it can be used as Github's Webhook)
Report is showed in **Allure Report**
Used: **Python** / **Playwright** / **requests**

There are 3 files, each one for different tests type

1. Web UI - test_UI.py / testdata_UI - https://automationintesting.online/ -> hotel booking page

2. API - test_API.py / testdata_API -  https://restful-booker.herokuapp.com/apidoc/index.html#api-Auth-CreateToken -> hotel booking page mathods

3. SQL - test_DB.py / testdata_DB - fake DB connections just to demonstrate backend automated tests with SQL -> using similar example for hotel booking system


-------------------------------- 1. UI ---------------------------------------------

Example tests I would create to test "Send Us a Message" (contact form) feature on the given Web App

1. Happy flow (with special chars)
2. Happy flow max chars
3. Happy flow min chars
4. Each of 5 field not correct - to little chars or empty
5. Each of 5 field not correct - to many chars
6. Email has no '@'
7. Multiple error messages at once
8. After attepting to isert bad data, it is still possible to Submit form with success
9. SQL injection test

Above is covered in 6 test methods run on 22 datasets with pytest parametrize. All written in test_main.py and testdata.py (when run from jenkins it is multiplayed by 3 browsers),

Note that: 

a) There are several test that fail. I'm aware of it and in my opinion these would be defects in real life scenarios. I added my comments in the code to mark them

b) Jenkins build is configured to not fail whole build if some tests fail

c) Passwords for API are not stored in secret.py file (only locally on my machine) but are setup as variables with Jenkins build


This is how it looks like run win VS Code

<img width="304" height="593" alt="image" src="https://github.com/user-attachments/assets/f5a9fd88-c3c6-4d36-82d8-abc831cbf2f7" />



And this is example Allure Report after build is finished. 
(Jenkins is configured to install needed packages on build and run all the tests with 'pytest --browser webkit --browser firefox --browser chromium --alluredir=report --junitxml=result.xml --html=report.html')

<img width="1073" height="675" alt="image" src="https://github.com/user-attachments/assets/8e5bba33-d18f-404e-a859-a4e01c35da45" />

<img width="1075" height="972" alt="image" src="https://github.com/user-attachments/assets/34d208f2-9b0f-495e-a8bf-4885c669fc05" />



Also part of logs from Jenkins build where tests were run:
(here there are 22 UI tests * 3 browsers + 6 API tests)

<img width="523" height="19" alt="image" src="https://github.com/user-attachments/assets/81308b36-29c6-4f31-9d89-ec8cd6679961" />




-------------------------------- 2. API ---------------------------------------------

Simple example of tests, creation of booking, updating and later deleting test data within the fixture after 'yeald'

<img width="844" height="240" alt="image" src="https://github.com/user-attachments/assets/ed42edd2-2330-4347-97e7-8a68fd604d1f" />




-------------------------------- 3. Beckend SQL ---------------------------------------------

For automated backend testing with SQL I imagined scenario of migrating from Legacy DB to new one. As this DBs and scenario is faked this won't work in current setup. This is to showoff how this may be written.

Program has fixtures to set DB connetions in conftest.py. In test_DB.py it has test_ method to simulate scenario of testing migration one booking record from one DB to another. It has related 2 methods for running SQL procedure to run the synchronisation and other one to conmpare actuall and expected SQL results.
