from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from pages.PuyaSubs import puya
import os
import sys


def clean():
    clearScreen = os.system('cls')


def closeDriver(driver):
    driver.close()


def initializeDriver(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-infobars")
    chromeDriver = webdriver.Chrome(executable_path='chromedriver.exe',chrome_options=chrome_options)
    chromeDriver.get(url)
    return chromeDriver


print("       - Welcome Senpai! to ANIMU-SAN v.1.0.0 - \n")

driver = initializeDriver('http://www.puya.si')
match = puya(driver, 'Joshi Kausei','Monster Strike – The Animation – 39')
if not match:
    print("No match!")
closeDriver(driver)













