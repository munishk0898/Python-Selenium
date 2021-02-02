import time
from selenium.webdriver.common.by import By
import library.Driver as D

USERNAME_INPUT = (By.NAME, 'email')
PASSWORD_INPUT = (By.NAME, 'password')
REMEMBER_ME = (By.NAME, 'remember')
FORGOT_PASSWORD = (By.ID, 'link-forgot')
LOGIN_BUTTON = (By.CLASS_NAME, 'btn-lg')
LOGOUT = (By.ID, 'logout')


def is_url_reachable():
    D.driver_instance.get("https://www.phptravels.net/admin")
    return D.driver_instance.title


def web_login(user):
    username = user[0]
    password = user[1]
    D.driver_instance.find_element(*USERNAME_INPUT).send_keys(username)
    D.driver_instance.find_element(*PASSWORD_INPUT).send_keys(password)
    D.driver_instance.find_element(*LOGIN_BUTTON).click()
    time.sleep(10)
    return bool(D.driver_instance.find_element(*LOGOUT))
