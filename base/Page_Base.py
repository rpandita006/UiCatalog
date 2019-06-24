import unittest
from appium import webdriver

__author__ = 'sanjyotj'


class SetUpDriver():
    def setup(self):
        # Set up appium
        self.driver = webdriver.Remote(
            command_executor='http://0.0.0.0:4723/wd/hub',
            desired_capabilities={
                'app': '/Users/synerzip/Desktop/UICatalog.app',
                'platformName': 'iOS',
                'automationName': 'XCUITest',
                'bundleID': 'com.demo.UICatalog123',
                'platformVersion': '12.2',
                'deviceName': 'iPhone X'
            })

    def tearDown(self):
        self.driver.quit()

    def __init__(self):
        super().__init__()
        self.is_open = False
        print("Initializing")
        self.setup()
