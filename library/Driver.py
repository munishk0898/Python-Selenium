from selenium import webdriver

driver_instance = None


def Initialize():
    global driver_instance
    driver_instance= webdriver.Chrome()
    driver_instance.implicitly_wait(5)
    return driver_instance


def CloseDriver():
    global driver_instance
    driver_instance.quit()
