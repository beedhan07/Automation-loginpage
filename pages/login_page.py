import time
from selenium.webdriver.common.by import By
from locator.locate import Locators

class login:
    def __init__(self,driver):
        self.driver = driver
        self.lc = Locators

    def login(self,username, password):
        driver = self.driver
        Nav_signin = driver.find_element(By.XPATH, self.lc.nav_login_Xpath)
        Nav_signin.click()

        nav_username = driver.find_element(By.ID, self.lc.txt_username_id)
        nav_username.clear()
        nav_username.send_keys(username)
        driver.implicitly_wait(10)

        nav_password = driver.find_element(By.ID, self.lc.txt_password_id)
        nav_password.clear()
        nav_password.send_keys(password)
        driver.implicitly_wait(10)

        sign_button = driver.find_element(By.XPATH, self.lc.login_button_xpath)
        sign_button.click()
        time.sleep(3)
        homepage = driver.find_element(By.XPATH, self.lc.homepage_Xpath)
        homepage.click()
        time.sleep(5)

