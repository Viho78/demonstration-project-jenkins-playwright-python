# demonstration-project-jenkins-playwright-python
Demonstration project for python automated testing with usage of playwright / jenkins and other
Juliusz Stańczyk

Tests are integrated from my local machine to **Git/Jenkins** with use of **SocketXP** (it casts localhost to public address so it can be used as Github's Webhook)
Report is showed in **Allure Report**
Used: **Python** / **Playwright**

There are 3 files, each one for different tests type
Web UI - https://automationintesting.online/ -> hotel booking page

API - https://automationintesting.online/ -> hotel booking page

SQL - ?



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

Which results in X tests with Y dataset to test with, all written in test_main.py and testdata.py (when run from jenkins it is multiplayed with 3 browsers)
Note: There are several test that fail. I'm aware of it and in my opinion these are defects. I added my comments in the code
