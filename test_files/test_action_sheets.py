import unittest
from base import *
from pages import *


class ActionsPage(SetUpDriver):

    def test_action(self):
        driver = self.driver
        action_page = ActionSheet(driver)
        action_page.search_field()


if __name__ == '__main__':
    unittest.main()
