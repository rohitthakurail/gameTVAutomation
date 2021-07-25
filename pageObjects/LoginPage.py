from appium import webdriver

class LoginPage:
    twitter_login_button_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout//*[@class='android.widget.ImageView'][2]"
    def __init__(self,driver):
        self.driver = driver
    def get_twitter_button(self):
        twitter_login_button = self.driver.find_element_by_xpath(self.twitter_login_button_xpath)
        return twitter_login_button
    def clickTwitterButton(self):
        self.driver.find_element_by_xpath(self.twitter_login_button_xpath).click()
        
