from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    USERNAME_INPUT = (By.CSS_SELECTOR, '[id*=\"username\"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[id*=\"password\"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[class*=\"button--primary\"]')