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
ACCOUNTS = (By.XPATH, '//a[contains(@href,"#ACCOUNTS")]')


def is_url_reachable():
    D.driver_instance.get("https://www.phptravels.net/admin")
    return D.driver_instance.title


def web_login(user):
    username = user[0]
    password = user[1]
    D.driver_instance.find_element(*USERNAME_INPUT).send_keys(username)
    D.driver_instance.find_element(*PASSWORD_INPUT).send_keys(password)
    D.driver_instance.find_element(*LOGIN_BUTTON).click()
    time.sleep(5)
    return True


def expect_wrong_login_message():
    message = D.driver_instance.find_element(*LOGIN_MESSAGE)
    if message:
        print(message.text)
        return message.text
    else:
        raise Exception("Error Message not found")
    # return D.driver_instance.find_element(*LOGIN_MESSAGE).text


def current_driver_title():
    return D.driver_instance.title
