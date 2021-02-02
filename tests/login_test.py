from library import Login
from data import Webpage_elements as data
import pytest
import library.Driver as D


def setup():
    D.Initialize()


def test_is_url_reachable():
    assert Login.is_url_reachable()


def test_login():
    assert Login.web_login(data.login_credentials)


def teardown():
    D.CloseDriver()
