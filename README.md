# demonstration-project-jenkins-playwright-python
Demonstration project for python automated testing with usage of playwright / jenkins and other
Juliusz Stańczyk

Tests are integrated from my local machine to **Git/Jenkins** with use of **SocketXP** (it casts localhost to public address so it can be used as Github's Webhook)
Report is showed in **Allure Report**
Used: **Python** / **Playwright**

There are 3 files, each one for different tests type

Web UI - test_UI.py / testdata_UI - https://automationintesting.online/ -> hotel booking page

API - test_API.py / testdata_API -  https://automationintesting.online/ -> hotel booking page

SQL - not done yet - ?



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

Above is covered in 6 test functions run on 22 datasets with pytest parametrize. All written in test_main.py and testdata.py (when run from jenkins it is multiplayed by 3 browsers),
Note: There are several test that fail. I'm aware of it and in my opinion these would be defects in real life scenarios. I added my comments in the code to mark them.

This is how it looks like run win VS Code

<img width="304" height="593" alt="image" src="https://github.com/user-attachments/assets/f5a9fd88-c3c6-4d36-82d8-abc831cbf2f7" />



And this is example Allure Report after build is finished. 
(Jenkins is configured to install needed packages on build and run all the tests with 'pytest --browser webkit --browser firefox --browser chromium --alluredir=report --junitxml=result.xml --html=report.html')

<img width="1144" height="609" alt="image" src="https://github.com/user-attachments/assets/8f95dc6f-fd4f-419a-9300-502955804770" />

<img width="983" height="851" alt="image" src="https://github.com/user-attachments/assets/e97493d0-cdaf-46e4-9036-264566451bd9" />
