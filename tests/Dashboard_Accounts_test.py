import time
from library import Dashboard
from data import Webpage_elements as data
from library import Login
import library.Driver as D
import pytest


def setup():
    D.Initialize()


@pytest.mark.parametrize("j", data.DROPDOWN_SUBMENU_LIST)
@pytest.mark.parametrize("i", data.dropdown_elements)
def test_dropdown(i, j):

    assert Login.web_login(data.login_credentials)
    print(Dashboard.click_dropdown_get_list_elements(i))


def teardown():
    D.CloseDriver()
