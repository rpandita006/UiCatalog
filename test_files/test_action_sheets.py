import unittest
import pages


class Test_case1(unittest.TestCase):
    def test_action(self):
        pages.action_obj.search_field()

if __name__ == '__main__':
    unittest.main()
