import time
from selenium.webdriver.common.by import By
import library.Driver as D

USERNAME_INPUT = (By.NAME, 'email')
PASSWORD_INPUT = (By.NAME, 'password')
REMEMBER_ME = (By.NAME, 'remember')
FORGOT_PASSWORD = (By.ID, 'link-forgot')
LOGIN_BUTTON = (By.CLASS_NAME, 'btn-lg')
LOGOUT = (By.ID, 'logout')
LOGIN_MESSAGE = (By.CLASS_NAME, 'alert')


def is_url_reachable():
    D.driver.get("https://www.phptravels.net/admin")
    return D.driver.title


def web_login(user):
    username = user[0]
    password = user[1]
    D.driver.find_element(*USERNAME_INPUT).send_keys(username)
    D.driver.find_element(*PASSWORD_INPUT).send_keys(password)
    D.driver.find_element(*LOGIN_BUTTON).click()
    time.sleep(5)
    return True


def expect_wrong_login_message():
    message = D.driver.find_element(*LOGIN_MESSAGE)
    if message:
        print("Expected Error message: ", message.text)
        return message.text
    else:
        raise Exception("Error Message not found")


def current_driver_title():
    return D.driver.title
