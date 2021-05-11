import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from confirmer import sendConfirmation
from confirmer import sendError

load_dotenv()

PATH = os.getenv('DRIVER_PATH')
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(PATH)
usr = os.getenv('CNC_USR')
pw = os.getenv('CNC_PW')


def elementExists(val, type):
    if type == 'id':
        try:
            driver.find_element_by_id(val)
            return True
        except:
            return False
    elif type == 'inner':
        try:
            driver.find_element_by_link_text(val)
            return True
        except:
            return False


def clocker():
    # start
    driver.get("https://www.cnc-claimsource.com/")

    # login page
    usrInput = driver.find_element_by_id("username")
    pwInput = driver.find_element_by_id("password")
    submitBtn = driver.find_element_by_id("loginBtn")

    usrInput.send_keys(usr)
    pwInput.send_keys(pw)
    submitBtn.click()

    # claimsource panel
    if elementExists("Click here to access the time clock", 'inner'):
        panel = driver.find_element_by_link_text(
            "Click here to access the time clock")
        panel.click()
    else:
        # likely have been redirected to password update page
        print('Error clocking')
        sendError()
        driver.quit()
        return

    # clock page
    clocker = False
    isClockingIn = True
    if elementExists('clockin', 'id'):
        clocker = driver.find_element_by_id('clockin')
    elif elementExists('clockout', 'id'):
        clocker = driver.find_element_by_id('clockout')
        isClockingIn = False

    if clocker != False:
        clocker.click()
        sendConfirmation(isClockingIn)
        print('Clocked In' if isClockingIn else 'Clocked Out')
    else:
        print('error')
        sendError()

    driver.quit()
    return


clocker()
