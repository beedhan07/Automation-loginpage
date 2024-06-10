import unittest
from selenium import webdriver
from pages.login_page import login

class MyTestCase(unittest.TestCase):

     def setUp(self):
         self.driver = webdriver.Chrome()
         self.driver.maximize_window()
         self.driver.get("https://qaecomb.bishalkarki.xyz/")

     def test_something(self):
         self.lp = login(self.driver)
         self.lp.login("beedhan36@gmail.com","Bidhan12!@")



if __name__ == '__main__':
    unittest.main()
