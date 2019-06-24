from time import sleep
from base import *


# This class contains methods to login to the url with the credentials.
class Action(SetUpDriver):
    def search_field(self):
        print('hello')
        action_ele = self.driver.find_element_by_name("Action Sheets")
        sleep(2)
        action_ele.click()
        other_ele = self.driver.find_element_by_name("Other")
        sleep(2)
        other_ele.click()
        choice_ele = self.driver.find_element_by_name("Safe Choice")
        sleep(2)
        choice_ele.click()
