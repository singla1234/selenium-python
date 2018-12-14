from selenium import webdriver
import unittest
import HtmlTestRunner
class GoogleSearch(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
     cls.driver = webdriver.Chrome(executable_path='chromedriver.exe')
     cls.driver.implicitly_wait(10)
     cls.driver.maximize_window()

 def test_search_automationstepbystep(self):
     self.driver.get("https://google.com")
     self.driver.find_element_by_name("q").send_keys("Automation Step by Step")
     self.driver.find_element_by_name("btnK").click()

 def test_search_automationstepbystep(self):
     self.driver.get("https://google.com")
     self.driver.find_element_by_name("q").send_keys("Raghav pal")
     self.driver.find_element_by_name("btnK").click()
 @classmethod
 def tearDownClass(cls):
     cls.driver.close()
     cls.driver.quit()
 print("Test Completed")
if __name__ == '__main__':
 unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/gur29899/PycharmProjects/selenium-python/reports/'))