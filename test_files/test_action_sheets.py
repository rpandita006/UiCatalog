import unittest
from base import *
from pages import *


class ActionsPage(SetUpDriver):

    def test_action(self):
        driver = self.driver
        ActionPage = ActionSheet(driver)
        ActionPage.search_field()


if __name__ == '__main__':
    unittest.main()
