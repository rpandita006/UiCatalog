from time import sleep


class ActionSheet(object):

    def __init__(self, driver):
        self.driver = driver

    def search_field(self):
        print('hello')
        action_ele = self.driver.find_element_by_name("Action Sheets")
        action_ele.click()
        other_ele = self.driver.find_element_by_name("Other")
        sleep(2)
        other_ele.click()
        choice_ele = self.driver.find_element_by_name("Safe Choice")
        sleep(2)
        choice_ele.click()
