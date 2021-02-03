import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
"""
USERNAME_INPUT = By.NAME, 'email'
PASSWORD_INPUT = (By.NAME, 'password')
LOGIN_BUTTON = (By.CLASS_NAME, 'btn-lg')
message = By.CLASS_NAME,'resultlogin'
driver = webdriver.Chrome()
driver.get('https://www.phptravels.net/admin')
driver.find_element(*USERNAME_INPUT).send_keys('admin')
driver.find_element(*PASSWORD_INPUT).send_keys('demoadmin')
driver.find_element(*LOGIN_BUTTON).click()
time.sleep(2)
print(driver.title)
time.sleep(2)
print(driver.find_element(*message).text)
"""
dropdown_elements = ['ACCOUNTS', 'CMS', 'HOTELS', 'FLIGHTS', 'BOATS', 'RENTALS', 'TOURS', 'CARTRAWLER', 'VISA', 'BLOG',
                     'LOCATIONS',
                     'OFFERS', 'PAYOUTS']
dropdown_list_elements = ['Accounts', 'CMS', 'Hotels', 'Flights', 'Boats', 'Rentals', 'TOURS', 'CARTRAWLER', 'VISA',
                          'BLOG', 'LOCATIONS',
                          'OFFERS', 'PAYOUTS']
for i in range(0,len(dropdown_elements)):
    print(dropdown_elements[i]+"=("+"By.ID,"+dropdown_list_elements[i]+")")
