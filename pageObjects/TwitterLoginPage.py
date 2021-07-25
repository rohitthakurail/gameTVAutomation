from appium import webdriver

class TwitterLoginPage:
    username_and_password_textbox_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout//*[@class='android.widget.EditText']"
    authorize_button_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout//*[@class='android.widget.Button'][@index='0']"
    elemensts_on_home_screen_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout//*[@class='android.widget.ImageView'][@index='0']"

    def __init__(self,driver):
        self.driver = driver

    def setUserNameandPassword(self,username,password):
        self.username_field = self.driver.find_elements_by_xpath(self.username_and_password_textbox_xpath)[0]
        self.password_field = self.driver.find_elements_by_xpath(self.username_and_password_textbox_xpath)[1]
        self.username_field.clear()
        self.username_field.send_keys(username)
        self.password_field.clear()
        self.password_field.send_keys(password)

    def clickAuthorize(self):
        self.driver.find_element_by_xpath(self.authorize_button_xpath).click()

    def getElementsHomeScreen(self):
        elems_on_home_scrren = self.driver.find_elements_by_xpath(self.elemensts_on_home_screen_xpath)
        return elems_on_home_scrren
