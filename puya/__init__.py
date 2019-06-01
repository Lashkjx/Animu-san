from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from UI.PuyaSubs import puya
from pages.Spreadsheet import *
import os


def clean():
    clearScreen = os.system('cls')


def closeDriver(driver):
    driver.close()


def initialize(browser,url):
    if browser == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chromeDriver = webdriver.Chrome(executable_path='chromedriver.exe',chrome_options=chrome_options)
        chromeDriver.get(url)
        return chromeDriver
    elif browser == "firefox":
        options = Options()
        options.headless = True
        firefoxDriver = webdriver.Firefox(options=options, executable_path=r'geckodriver.exe')
        firefoxDriver.get(url)
        return firefoxDriver

print("       - Welcome Senpai! to ANIMU-SAN v.1.0.0 - \n")

driver = initialize("firefox", 'http://www.puya.moe')
animeEntries = animeEntriesGS()
animeStop = animeStopGS()
for anime in animeEntries:
    driver = puya(driver, anime, animeStop)
closeDriver(driver)













