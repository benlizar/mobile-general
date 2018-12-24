from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import *


class PageScreen:

    def __init__(self, driver):
        self.driver = driver

    def log_user(self):

        login_button = WebDriverWait(self.driver.instance, 15).until(
            EC.visibility_of_element_located((
                MobileBy.XPATH, "//android.widget.Button"
            ))
        )
        login_button.click()

        self.switch_context("WEBVIEW_chrome")

        textbox_username = WebDriverWait(self.driver.instance, 7000).until(
            EC.visibility_of_element_located((
                MobileBy.XPATH, "//input[@name='username']"
            ))
        )

        textbox_password = WebDriverWait(self.driver.instance, 2).until(
            EC.visibility_of_element_located((
                MobileBy.XPATH, "//input[@name='password']"
            ))
        )

        button_login = WebDriverWait(self.driver.instance, 2).until(
            EC.visibility_of_element_located((
                MobileBy.XPATH, "//button[@name='submit']"
            ))
        )
        self.fill_user_data(textbox_username, textbox_password)
        button_login.click()

        assert self.verify_user_login()

    def switch_context(self, new_context):

        c_context = self.driver.instance.mobile.contexts
        self.driver.instance.switch_to.context(new_context)

    def fill_user_data(self, username, password):
        username.send_keys(login_user)
        password.send_keys(login_password)

    def verify_user_login(self):
        self.switch_context("NATIVE_APP")

        alert_ok = WebDriverWait(self.driver.instance, 15).until(
            EC.visibility_of_element_located((
                MobileBy.XPATH, "//android.widget.Button"
            ))
        )
        alert_ok.click()

        button_logged = WebDriverWait(self.driver.instance, 15).until(
            EC.visibility_of_element_located((
                MobileBy.XPATH, "//android.widget.Button"
            ))
        )
        return True
