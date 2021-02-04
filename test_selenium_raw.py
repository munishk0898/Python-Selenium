import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

GENERAL = [(By.XPATH, '//a[contains(@href,"#menu-ui")]'), (By.XPATH, "//ul[@id='menu-ui']/li//a")]
USERNAME_INPUT = By.NAME, 'email'
PASSWORD_INPUT = (By.NAME, 'password')
LOGIN_BUTTON = (By.CLASS_NAME, 'btn-lg')
message = By.CLASS_NAME,'resultlogin'
driver = webdriver.Chrome()
driver.get('https://www.phptravels.net/admin')
driver.find_element(*USERNAME_INPUT).send_keys('admin@phptravels.com')
driver.find_element(*PASSWORD_INPUT).send_keys('demoadmin')
driver.find_element(*LOGIN_BUTTON).click()
time.sleep(5)
driver.find_element(*GENERAL[0]).click()
time.sleep(3)
elements = driver.find_elements(*GENERAL[1])
l = []
for i in elements:
    l.append(i.text)
print(l)

"""
dropdown_elements = ['ACCOUNTS', 'CMS', 'HOTELS', 'FLIGHTS', 'BOATS', 'RENTALS', 'TOURS', 'CARTRAWLER', 'VISA', 'BLOG',
                     'LOCATIONS',
                     'OFFERS', 'PAYOUTS']
dropdown_list_elements = ['Accounts', 'CMS', 'Hotels', 'Flights', 'Boats', 'Rentals', 'TOURS', 'CARTRAWLER', 'VISA',
                          'BLOG', 'LOCATIONS',
                          'OFFERS', 'PAYOUTS']
for i in range(0,len(dropdown_elements)):
    print(dropdown_elements[i]+"=("+"By.ID,"+dropdown_list_elements[i]+")")
"""

