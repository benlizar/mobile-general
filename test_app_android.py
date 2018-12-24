import unittest

from page_screen_android import PageScreen
from mobile_driver import Driver
from os_enum import OSEnum


class LockTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = Driver(OSEnum.ANDROID)

    def test_login_user(self):
        screen = PageScreen(self.driver)
        screen.log_user()

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LockTestCase)
    unittest.TextTestRunner().run(suite)
