from time import sleep


class ActionSheet(object):

    def __init__(self, driver):
        self.driver = driver

        self.action_ele = self.driver.find_element_by_name("Action Sheets")
        self.other_ele = self.driver.find_element_by_name("Other")
        self.choice_ele = self.driver.find_element_by_name("Safe Choice")
        self.back_ele = self.driver.find_element_by_name("Back")

    def search_field(self):
        print('In Actions')
        self.action_ele.click()
        sleep(2)
        self.other_ele.click()
        sleep(2)
        self.choice_ele.click()
        sleep(2)
        self.back_ele.click()

