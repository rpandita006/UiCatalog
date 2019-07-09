import unittest
from base import *
from pages import *

class LoginPage(SetUpDriver):

    def test_action(self):
       # driver = self.driver
        #action_page = ActionSheet(driver)
        # action_page.search_field()

           self.driver.get("https://orange.examsoft.com/GKWeb/login/QATWO")
           self.driver.find_element_by_id('userid').send_keys("rvarela+3@examsoft.com")
           self.driver.find_element_by_id('password').send_keys("password1")
           self.driver.find_element_by_id('emLoginLink').click()
           self.driver.find_element_by_xpath("//a[@class='navigation assessments']").click()


if __name__ == '__main__':
    unittest.main()
