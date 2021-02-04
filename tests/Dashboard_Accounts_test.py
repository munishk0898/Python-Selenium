import time
from library import Dashboard
from data import Webpage_elements as data
from library import Login
import library.Driver as D
import pytest


def setup():
    D.Initialize()


def test_dropdown():
    assert Login.web_login(data.login_credentials)
    for i in range(len(data.dropdown_elements)):
        assert Dashboard.click_dropdown_get_list_elements(data.dropdown_elements[i]) == data.DROPDOWN_SUBMENU_LIST[i]


def teardown():
    D.CloseDriver()
