import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Webdrivers import *


class LoginPage:
    USERNAME_INPUT = (By.NAME, 'email')
    PASSWORD_INPUT = (By.NAME, 'password')
    REMEMBER_ME = (By.NAME, 'remember')
    FORGOT_PASSWORD = (By.ID, 'link-forgot')
    LOGIN_BUTTON = (By.CLASS_NAME, 'btn-lg')
    LOGOUT = (By.ID, 'logout')


    def login(self, user):
        driver = webdriver.Chrome()
        username = user[0]
        password = user[1]
        print(username)
        print(password)
        
        driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*self.LOGIN_BUTTON).click()
        time.sleep(10)
        return self.driver.find_element(*self.LOGOUT)
