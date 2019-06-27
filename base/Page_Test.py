import unittest
from appium import webdriver

__author__ = 'sanjyotj'


class SetUpDriver(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('Initializing')
        cls.driver = webdriver.Remote(
            command_executor='http://0.0.0.0:4723/wd/hub',
            desired_capabilities={
                'app': '/Users/synerzip/Desktop/UICatalog.app',
                'platformName': 'iOS',
                'automationName': 'XCUITest',
                'bundleID': 'com.demo.UICatalog123',
                'platformVersion': '12.2',
                'deviceName': 'iPhone X',
                'useNewWDA': 'true',
                'waitForQuiescence': 'false'
            })

    @classmethod
    def tearDownClass(cls) -> None:
        print('Terminating')
        cls.driver.quit()
