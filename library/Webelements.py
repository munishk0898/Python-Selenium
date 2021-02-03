import time
from selenium.webdriver.common.by import By
import library.Driver as D

ACCOUNTS = (By.ID, 'Accounts')
CMS = (By.ID, 'CMS')
HOTELS = (By.ID, 'Hotels')
FLIGHTS = (By.ID, 'Flights')
BOATS = (By.ID, 'Boats')
RENTALS = (By.ID, 'Rentals')
TOURS = (By.ID, 'TOURS')
CARTRAWLER = (By.ID, 'CARTRAWLER')
VISA = (By.ID, 'VISA')
BLOG = (By.ID, 'BLOG')
LOCATIONS = (By.ID, 'LOCATIONS')
OFFERS = (By.ID, 'OFFERS')
PAYOUTS = (By.ID, 'PAYOUTS')


def get_list_elements(i):
    if label == 'ACCOUNTS':
        D.driver_instance.find_element(*ACCOUNTS).click()
        elements = D.driver_instance.find_elements(*i)
        for i in elements:
            print(i.text)
    elif label == "CMS":
        D.driver_instance.find_element(*CMS).click()
    elif label == "HOTELS":
        D.driver_instance.find_element(*HOTELS).click()
    elif label == "FLIGHTS":
        D.driver_instance.find_element(*FLIGHTS).click()
    elif label == "BOATS":
        D.driver_instance.find_element(*BOATS).click()
    elif label == "RENTALS":
        D.driver_instance.find_element(*RENTALS).click()
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
    elements = D.driver_instance.find_elements(*i)
    for i in elements:
        print(i.text)