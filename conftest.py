from data import Webpage_elements
from selenium import webdriver
import pytest


@pytest.fixture()
def config_data():
    data = Webpage_elements
    return data


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver
