import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
USERNAME_INPUT = By.NAME, 'email'
driver = webdriver.Chrome()
driver.get('https://www.phptravels.net/admin')
driver.find_element(*USERNAME_INPUT).send_keys('Munish')

"""


def setup():
    print("Running before every test")


def test_1():
    print("First")


def test_2():
    print("Second")

