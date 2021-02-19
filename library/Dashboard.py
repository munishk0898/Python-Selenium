import time
from selenium.webdriver.common.by import By
import library.Driver as D
import library.utils

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
UPDATES = (By.XPATH, '//*[@id="social-sidebar-menu"]/li[2]/a')


def get_text_list(elements):
    list_text_elements = []
    for i in elements:
        list_text_elements.append(i.text)
    return list_text_elements


def click_dropdown_get_list_elements(label):
    if label == "GENERAL":
        D.driver.find_element(*GENERAL[0]).click()
        time.sleep(3)
        elements = D.driver.find_elements(*GENERAL[1])
    elif label == 'ACCOUNTS':
        D.driver.find_element(*ACCOUNTS[0]).click()
        time.sleep(3)
        elements = D.driver.find_elements(*ACCOUNTS[1])
    elif label == "CMS":
        D.driver.find_element(*CMS[0]).click()
        time.sleep(3)
        elements = D.driver.find_elements(*CMS[1])
    elif label == "HOTELS":
        D.driver.find_element(*HOTELS[0]).click()
        time.sleep(3)
        elements = D.driver.find_elements(*HOTELS[1])
    elif label == "FLIGHTS":
        D.driver.find_element(*FLIGHTS[0]).click()
        time.sleep(3)
        elements = D.driver.find_elements(*FLIGHTS[1])
    elif label == "BOATS":
        D.driver.find_element(*BOATS[0]).click()
        time.sleep(3)
        elements = D.driver.find_elements(*BOATS[1])
    elif label == "RENTALS":
        D.driver.find_element(*RENTALS[0]).click()
        time.sleep(3)
        elements = D.driver.find_elements(*RENTALS[1])
    elif label == "TOURS":
        D.driver.find_element(*TOURS[0]).click()
        time.sleep(3)
        elements = D.driver.find_elements(*TOURS[1])
    elif label == "CARTRAWLER":
        D.driver.find_element(*CARTRAWLER[0]).click()
        time.sleep(3)
        elements = D.driver.find_elements(*CARTRAWLER[1])
    elif label == "VISA":
        D.driver.find_element(*VISA[0]).click()
        time.sleep(3)
        elements = D.driver.find_elements(*VISA[1])
    elif label == "BLOG":
        D.driver.find_element(*BLOG[0]).click()
        time.sleep(3)
        elements = D.driver.find_elements(*BLOG[1])
    elif label == "LOCATIONS":
        D.driver.find_element(*LOCATIONS[0]).click()
        time.sleep(3)
        elements = D.driver.find_elements(*LOCATIONS[1])
    elif label == "OFFERS":
        D.driver.find_element(*OFFERS[0]).click()
        time.sleep(3)
        elements = D.driver.find_elements(*OFFERS[1])
    elif label == "PAYOUTS":
        D.driver.find_element(*PAYOUTS[0]).click()
        time.sleep(3)
        elements = D.driver.find_elements(*PAYOUTS[1])
    else:
        raise Exception("Expected", label, " dropdown not Found")
    return get_text_list(elements)


def get_text(element):
    label_text = D.driver.find_element(*element)
    return label_text.text


def click_element(element):
    update_str = D.driver.find_element(*element)
    update_str.click()
    return True
