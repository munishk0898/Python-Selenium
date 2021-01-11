from library.Login import LoginPage
from data import *
import pytest


def test_login(config_data):
    assert LoginPage.login(*config_data.login_credentials)
