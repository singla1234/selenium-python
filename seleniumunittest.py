import unittest
from selenium import webdriver


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()


    def test_something(self):
        self.assertEqual(True, False)


