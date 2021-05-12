import os
import sys
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
driver = webdriver.Chrome(executable_path=PATH, options=chrome_options)
usr = os.getenv('CNC_USR')
pw = os.getenv('CNC_PW')

checkLoginStatus = False
if len(sys.argv) > 1:
    checkLoginStatus = sys.argv[1] == '--check'


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


def statusChecker():
    # clock page
    if elementExists('clockin', 'id'):
        print('Currently Clocked Out')
    elif elementExists('clockout', 'id'):
        print('Currently Clocked In')
    return


def clocker():
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
    return


def main():
    # start
    print("Spinning up warp drive...🚀")
    driver.get("https://www.cnc-claimsource.com/")

    # login page
    usrInput = driver.find_element_by_id("username")
    pwInput = driver.find_element_by_id("password")
    submitBtn = driver.find_element_by_id("loginBtn")

    usrInput.send_keys(usr)
    pwInput.send_keys(pw)
    submitBtn.click()

    # claimsource panel
    if not elementExists("Click here to access the time clock", 'inner'):
        # likely have been redirected to password update page
        print('Error clocking, you probably are required to change your password')
        sendError()
    else:
        panel = driver.find_element_by_link_text(
            "Click here to access the time clock")
        panel.click()
        if checkLoginStatus:
            statusChecker()
        else:
            clocker()

    driver.quit()
    return


main()
