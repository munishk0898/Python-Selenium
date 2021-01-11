import time
from selenium import webdriver
from selenium.webdriver.common.by import By

USERNAME_INPUT = (By.NAME, 'email')
PASSWORD_INPUT = (By.NAME, 'password')
REMEMBER_ME = (By.NAME, 'remember')
FORGOT_PASSWORD = (By.ID, 'link-forgot')
LOGIN_BUTTON = (By.CLASS_NAME, 'btn-lg')
LOGOUT = (By.ID, 'logout')


def web_driver():
    login_driver = webdriver.Chrome()
    print("First Driver")
    print(login_driver)
    login_driver.maximize_window()
    return login_driver


def is_url_reachable(url):
    driver = web_driver()
    driver.get(url)
    return driver.title


def web_login(url, user):
    driver = web_driver()
    driver.get(url)
    username = user[0]
    password = user[1]
    print(type(driver))
    driver.find_element(USERNAME_INPUT).send_keys(username)
    driver.find_element(PASSWORD_INPUT).send_keys(password)
    driver.find_element(LOGIN_BUTTON).click()
    time.sleep(10)
    return bool(driver.find_element(LOGOUT))
