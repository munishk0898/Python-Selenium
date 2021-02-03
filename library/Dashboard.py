import time
from selenium.webdriver.common.by import By
import library.Driver as D

GENERAL = [(By.XPATH, '//a[contains(@href,"#menu-ui")]'), (By.ID, 'Accounts')]
ACCOUNTS = [(By.XPATH, '//a[contains(@href,"#ACCOUNTS")]'), (By.ID, 'Accounts')]
CMS = [(By.XPATH, '//a[contains(@href,"#CMS")]'), (By.ID, 'CMS')]
HOTELS = [(By.XPATH, '//a[contains(@href,"#Hotels")]'), (By.ID, 'Hotels')]
FLIGHTS = [(By.XPATH, '//a[contains(@href,"#Flights")]'), (By.ID, 'Flights')]
BOATS = [(By.XPATH, '//a[contains(@href,"#Boats")]'), (By.ID, 'Boats')]
RENTALS = [(By.XPATH, '//a[contains(@href,"#Rentals")]'), (By.ID, 'Rentals')]
TOURS = [(By.XPATH, '//a[contains(@href,"#Tours")]'), (By.ID, 'TOURS')]
CARTRAWLER = [(By.XPATH, '//a[contains(@href,"#Cartrawler")]'), (By.ID, 'CARTRAWLER')]
VISA = [(By.XPATH, '//a[contains(@href,"#Ivisa")]'), (By.ID, 'VISA')]
BLOG = [(By.XPATH, '//a[contains(@href,"#Blog")]'), (By.ID, 'BLOG')]
LOCATIONS = [(By.XPATH, '//a[contains(@href,"#Locations")]'), (By.ID, 'LOCATIONS')]
OFFERS = [(By.XPATH, '//a[contains(@href,"#SPECIAL_OFFERS")]'), (By.ID, 'OFFERS')]
PAYOUTS = [(By.XPATH, '//a[contains(@href,"#PAYOUTS")]'), (By.ID, 'PAYOUTS')]


def click_dropdown_get_list_elements(label):
    if label == 'ACCOUNTS':
        D.driver_instance.find_element(*ACCOUNTS[0]).click()
        elements = D.driver_instance.find_elements(*ACCOUNTS[1])
        Accounts_elements = []
        for i in elements:
            Accounts_elements.append(i.text)
        return Accounts_elements
    elif label == "CMS":
        D.driver_instance.find_element(*CMS[0]).click()
        elements = D.driver_instance.find_elements(*CMS[1])
        for i in elements:
            print(i.text)
    elif label == "HOTELS":
        D.driver_instance.find_element(*HOTELS[0]).click()
        elements = D.driver_instance.find_elements(*HOTELS[1])
        for i in elements:
            print(i.text)
    elif label == "FLIGHTS":
        D.driver_instance.find_element(*FLIGHTS[0]).click()
        elements = D.driver_instance.find_elements(*ACCOUNTS[1])
        for i in elements:
            print(i.text)
    elif label == "BOATS":
        D.driver_instance.find_element(*BOATS[0]).click()
        elements = D.driver_instance.find_elements(*BOATS[1])
        for i in elements:
            print(i.text)
    elif label == "RENTALS":
        D.driver_instance.find_element(*RENTALS).click()
        elements = D.driver_instance.find_elements(*ACCOUNTS[1])
        for i in elements:
            print(i.text)
    elif label == "TOURS":
        D.driver_instance.find_element(*TOURS).click()

    elif label == "CARTRAWLER":
        D.driver_instance.find_element(*CARTRAWLER).click()
    elif label == "VISA":
        D.driver_instance.find_element(*VISA).click()
    elif label == "BLOG":
        D.driver_instance.find_element(*BLOG).click()
    elif label == "LOCATIONS":
        D.driver_instance.find_element(*LOCATIONS).click()
    elif label == "OFFERS":
        D.driver_instance.find_element(*OFFERS).click()
    elif label == "PAYOUTS":
        D.driver_instance.find_element(*PAYOUTS).click()
    else:
        raise Exception("Expected", label, " dropdown not Found")
