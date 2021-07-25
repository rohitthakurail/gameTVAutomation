import pytest
from appium import webdriver
import time
from pageObjects.TwitterLoginPage import TwitterLoginPage
from pageObjects.LoginPage import LoginPage
from testCases.configtest import setup as setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_Login:
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def testAppLaunch(self,setup):
        self.logger.info("************************ Starting testAppLauncher ***************************")
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.logger.info("************************ Verifying App Launch ***************************")
        twitter_login_button = self.lp.get_twitter_button()
        class_of_button = str(twitter_login_button.get_attribute("class"))
        desc_of_button = str(twitter_login_button.get_attribute("content-desc"))
        if class_of_button=="android.widget.ImageView" and desc_of_button=="AuthoriseWithTwitter_593":
            assert True
            self.logger.info("************************ testAppLauncher Passed ***************************")
        else:
            self.logger.error("************************ testAppLauncher Failed ***************************")
            assert False
        self.driver.quit()

    def test_login(self,setup):
        self.logger.info("************************ Starting testLogin ***************************")
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.lp.clickTwitterButton()
        self.tlp = TwitterLoginPage(self.driver)
        self.logger.info("************************ Logging in with Twitter ***************************")
        self.tlp.setUserNameandPassword(self.username,self.password)
        self.tlp.clickAuthorize()
        time.sleep(10)
        self.logger.info("************************ Verifying Home Screen with Hamberger Menu ***************************")
        elems_on_home_page = self.tlp.getElementsHomeScreen()
        desc_of_hamberger_menu= str(elems_on_home_page[0].get_attribute("content-desc"))
        if desc_of_hamberger_menu== 'SvgPicture_HamburgerIcon_001':
            assert True
            self.logger.info("************************ testLogin Passed ***************************")
        else:
            self.logger.error("************************ testLogin Failed ***************************")

            assert False
        self.driver.quit()