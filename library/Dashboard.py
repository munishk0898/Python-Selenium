import time
from selenium.webdriver.common.by import By
import library.Driver as D

GENERAL = [(By.XPATH, '//a[contains(@href,"#menu-ui")]'), (By.XPATH, "//ul[@id='menu-ui']/li//a")]
ACCOUNTS = [(By.XPATH, '//a[contains(@href,"#ACCOUNTS")]'), (By.XPATH, '//*[@id="ACCOUNTS"]//li//a')]
CMS = [(By.XPATH, '//a[contains(@href,"#CMS")]'), (By.XPATH, '//*[@id="CMS"]//li//a')]
HOTELS = [(By.XPATH, '//a[contains(@href,"#Hotels")]'), (By.XPATH, '//*[@id="Hotels"]//li//a')]
FLIGHTS = [(By.XPATH, '//a[contains(@href,"#Flights")]'), (By.XPATH, '//*[@id="Flights"]//li//a')]
BOATS = [(By.XPATH, '//a[contains(@href,"#Boats")]'), (By.XPATH, '//*[@id="Boats"]//li//a')]
RENTALS = [(By.XPATH, '//a[contains(@href,"#Rentals")]'), (By.XPATH, '//*[@id="Rentals"]//li//a')]
TOURS = [(By.XPATH, '//a[contains(@href,"#Tours")]'), (By.XPATH, '//*[@id="Tours"]//li//a')]
CARTRAWLER = [(By.XPATH, '//a[contains(@href,"#Cartrawler")]'), (By.XPATH, '//*[@id="Cartrawler"]//li//a')]
VISA = [(By.XPATH, '//a[contains(@href,"#Ivisa")]'), (By.XPATH, '//*[@id="Ivisa"]//li//a')]
BLOG = [(By.XPATH, '//a[contains(@href,"#Blog")]'), (By.XPATH, '//*[@id="Blog"]//li//a')]
LOCATIONS = [(By.XPATH, '//a[contains(@href,"#Locations")]'), (By.XPATH, '//*[@id="Locations"]//li//a')]
OFFERS = [(By.XPATH, '//a[contains(@href,"#SPECIAL_OFFERS")]'), (By.XPATH, '//*[@id="SPECIAL_OFFERS"]//li//a')]
PAYOUTS = [(By.XPATH, '//a[contains(@href,"#PAYOUTS")]'), (By.XPATH, '//*[@id="PAYOUTS"]//li//a')]
text_list = (By.TAG_NAME, 'a')


def get_text_list(elements):
    list_text_elements = []
    for i in elements:
        list_text_elements.append(i.text)
    return list_text_elements


def click_dropdown_get_list_elements(label):
    if label == "GENERAL":
        D.driver_instance.find_element(*GENERAL[0]).click()
        time.sleep(3)
        elements = D.driver_instance.find_elements(*GENERAL[1])
        print(get_text_list(elements))
        return True
    elif label == 'ACCOUNTS':
        D.driver_instance.find_element(*ACCOUNTS[0]).click()
        time.sleep(3)
        elements = D.driver_instance.find_elements(*ACCOUNTS[1])
        get_text_list(elements)
    elif label == "CMS":
        D.driver_instance.find_element(*CMS[0]).click()
        time.sleep(3)
        elements = D.driver_instance.find_elements(*CMS[1])
        get_text_list(elements)
    elif label == "HOTELS":
        D.driver_instance.find_element(*HOTELS[0]).click()
        time.sleep(3)
        elements = D.driver_instance.find_elements(*HOTELS[1])
        get_text_list(elements)
    elif label == "FLIGHTS":
        D.driver_instance.find_element(*FLIGHTS[0]).click()
        time.sleep(3)
        elements = D.driver_instance.find_elements(*FLIGHTS[1])
        get_text_list(elements)
    elif label == "BOATS":
        D.driver_instance.find_element(*BOATS[0]).click()
        time.sleep(3)
        elements = D.driver_instance.find_elements(*BOATS[1])
        get_text_list(elements)
    elif label == "RENTALS":
        D.driver_instance.find_element(*RENTALS[0]).click()
        time.sleep(3)
        elements = D.driver_instance.find_elements(*RENTALS[1])
        get_text_list(elements)
    elif label == "TOURS":
        D.driver_instance.find_element(*TOURS[0]).click()
        time.sleep(3)
        elements = D.driver_instance.find_elements(*TOURS[1])
        get_text_list(elements)
    elif label == "CARTRAWLER":
        D.driver_instance.find_element(*CARTRAWLER[0]).click()
        time.sleep(3)
        elements = D.driver_instance.find_elements(*CARTRAWLER[1])
        get_text_list(elements)
    elif label == "VISA":
        D.driver_instance.find_element(*VISA[0]).click()
        time.sleep(3)
        elements = D.driver_instance.find_elements(*VISA[1])
        get_text_list(elements)
    elif label == "BLOG":
        D.driver_instance.find_element(*BLOG[0]).click()
        time.sleep(3)
        elements = D.driver_instance.find_elements(*BLOG[1])
        get_text_list(elements)
    elif label == "LOCATIONS":
        D.driver_instance.find_element(*LOCATIONS[0]).click()
        time.sleep(3)
        elements = D.driver_instance.find_elements(*LOCATIONS[1])
        get_text_list(elements)
    elif label == "OFFERS":
        D.driver_instance.find_element(*OFFERS[0]).click()
        time.sleep(3)
        elements = D.driver_instance.find_elements(*OFFERS[1])
        get_text_list(elements)
    elif label == "PAYOUTS":
        D.driver_instance.find_element(*PAYOUTS[0]).click()
        time.sleep(3)
        elements = D.driver_instance.find_elements(*PAYOUTS[1])
        get_text_list(elements)
    else:
        raise Exception("Expected", label, " dropdown not Found")
