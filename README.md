# gameTVAutomation
Requirements:
1.	Install and launch the app. 
Verify that the user is able to launch the application and login screen is visible.
2.	Twitter Icon should be visible on the login screen and users should be able to click on it.
3.	User should be able to login to Game.tv through the twitter option. Use test account for login into game.tv using twitter credentials below
Creds: tes1.auto1@gmail.com
Password: game@twitter
4.	Once a user logs in successfully,  confirm it by verifying that you are on Home Page.
5.	Generate a consolidated report containing the status of each test case (clearly mentioning if a test case passed or failed)

Environment Setup:
Required Packages needs to be install for executing the project.
1. Appium-Python-Client(1.2.0)
2. nodeenv(1.6.0)
3. pytest(6.2.4)
4. pytest-html(3.1.1)
5. selenium(3.141.0)

Assumptions:
1. Only one Android Device connected to adb.
2. User provides UDID manually in config.ini file.

Implementation:
1. Started the Appium Sever
2. Got Locators and Created Page Object Model
3. Created Tests for required test cases
4. Assertion of actual output with expected output 
5. Created config.ini file to take values of variables used in test suite.
6. Configured Logger.
7. Configured pytest-html for generating reports of tests.

Important* 
1.There was some issue with provided twitter credentials(wrong username or password). 
2. Please provide UDID manually in config.ini file
