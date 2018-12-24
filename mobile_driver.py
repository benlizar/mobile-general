from appium import webdriver
from config import *
from os_enum import OSEnum


class Driver:

    def __init__(self, os_type: OSEnum):
        if os_type == OSEnum.ANDROID:
            self.instance = webdriver.Remote("http://127.0.0.1:4723/wd/hub", android_desired_caps)
        elif os_type == OSEnum.IOS:
            self.instance = webdriver.Remote("http://127.0.0.1:4723/wd/hub", ios_desired_caps)

