from selenium import webdriver

driver_instance = None


def Initialize():
    global driver_instance
    driver_instance= webdriver.Chrome()
    driver_instance.implicitly_wait(5)
    load_url = driver_instance.get("https://www.phptravels.net/admin")
    return load_url


def CloseDriver():
    global driver_instance
    driver_instance.quit()
