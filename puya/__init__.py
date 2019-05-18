from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pages.PuyaSubs import puya
from pages.Spreadsheet import *
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
animeEntries = animeEntriesGS()
animeStop = animeStopGS()
for anime in animeEntries:
    print("Title: " + anime)
    print("Stop: " + animeStop)
    driver = puya(driver, anime, animeStop)
closeDriver(driver)













