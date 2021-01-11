from library import Login
from data import Webpage_elements
import pytest


def test_url(config_data):
    assert Login.is_url_reachable(config_data.url) == config_data.Login_page_title


def test_login(config_data):
    print(config_data.login_credentials)
    assert Login.web_login(config_data.url, config_data.login_credentials)

