from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.mobile import Mobile
from config import *


class PageScreen:

    def __init__(self, driver):
        self.driver = driver

    def log_user(self):
        wait = WebDriverWait(self.driver.instance, 15)
        login_button = wait.until(
            EC.visibility_of_element_located((
                MobileBy.XPATH, "//android.widget.Button")))
        login_button.click()
        WebDriverWait(self.driver.instance, 15)

        self.switch_context("WEBVIEW")

        assert True

    def switch_context(self, new_context):

        c_context = self.driver.instance.mobile.contexts

        print(c_context)
        print("__BEFORE__")
        print(self.driver.instance.mobile.context)
        self.driver.instance.switch_to.context("WEBVIEW_chrome")
        print("__after__")
        print(self.driver.instance.mobile.context)

       # print(self.driver.instance.context + ": Before ")
       #  con = self.driver.instance.contexts
        # print(con)
       # self.driver.instance.context("WEBVIEW_chrome")
        #print(self.driver.instance.context + ": Before ")

