from appium import webdriver
import pytest
from utilities.readProperties import ReadConfig
from appium.webdriver.appium_service import AppiumService


@pytest.fixture()
def setup():
    appium_service = AppiumService()
    appium_service.start()
    dc = {}
    UDID = ReadConfig.getUDID()
    dc['udid'] = UDID
    dc['appPackage'] = 'tv.game'
    dc['appActivity'] = '.MainActivity'
    dc['platformName'] = 'android'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities=dc)
    driver.implicitly_wait(10)
    return driver


def pytest_configur(config):
    config.metadata['Project Name'] = 'GameTvAutomation'
    config.metadata['Module Name'] = 'Login'
    config.metadata['tester'] = 'Mr. Tester'

