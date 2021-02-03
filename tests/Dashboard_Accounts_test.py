import time
from library import Dashboard
from data import Webpage_elements as data
from library import Login
import library.Driver as D
import pytest


def setup():
    D.Initialize()


dropdown_elements = ['ACCOUNTS', 'CMS', 'HOTELS', 'FLIGHTS', 'BOATS', 'RENTALS', 'TOURS', 'CARTRAWLER', 'VISA', 'BLOG',
                     'LOCATIONS',
                     'OFFERS', 'PAYOUTS']
dropdown_list_elements = ['Accounts', 'CMS', 'Hotels', 'Flights', 'Boats', 'Rentals', 'TOURS', 'CARTRAWLER', 'VISA',
                          'BLOG', 'LOCATIONS',
                          'OFFERS', 'PAYOUTS']


def test_dropdown():
    assert Login.web_login(data.login_credentials)
    print(Dashboard.click_dropdown_get_list_elements("ACCOUNTS"))


def teardown():
    D.CloseDriver()
