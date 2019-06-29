from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from UI.PuyaSubs import puyaUI
from UI.MyAnimeList import *
from Rss.PuyaSubs import puyaRSS
from pages.Spreadsheet import *
from resources.API.Trello import *
from resources.CSV.CSV import *
from datetime import datetime, timedelta
import os
import keyboard


def isThatAMotherFuckingJojoReference(string):
    print('[Animu-san] Ara ara, you\'re approaching me?')
    print('[Kanan-chan] I can\'t {} without getting closer.'.format(string))

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

def executeUI():
    driver = initialize("firefox", 'http://www.puya.moe')
    animeEntries = animeEntriesGS()
    animeStop = animeStopGS()
    for anime in animeEntries:
        driver = puyaUI(driver, anime, animeStop)
    closeDriver(driver)

def executeRSS(animeEntries, lastEntry):
    for anime in animeEntries:
        last = puyaRSS(anime, lastEntry)
    return last

def initDownload():
    driver = initializeAnimuSan()
    animeEntries = animeEntriesGS(driver)
    lastEntry = getLastEntry(driver)
    entry = executeRSS(animeEntries, lastEntry)
    setLastEntry(driver, entry)

def updateSpreedsheet():
    cred = getCredentials()
    cards = getCards(cred[0], cred[1])
    driver = initializeAnimuChan()
    addEntry(driver, cards)

def findPattern():
    cred = getCredentials()
    sheet = initializeAnimuTan()
    title = input('[Animu-san] Please give me the title: ')
    animeData = getAnimeDataList(sheet, title)

def addSeries():
    title = input('[Animu-san] Please give me the title: ')
    episodes = input('[Animu-san] Please tell me the amount of episodes: ')
    addCustomCardSeries(title, episodes)

def addEpisodes():
    title = input('[Animu-san] Please give me the title: ')
    status = input('[Animu-san] Please give me the status: ')
    first = input('[Animu-san] Please tell me the first episode: ')
    last = input('[Animu-san] Pleass tell me the last episode: ')
    addCustomCardEpisodes(title, first, last, status)

def addEpisode():
    title = input('[Animu-san] Please give me the title: ')
    status = input('[Animu-san] Please give me the status: ')
    episode = input('[Animu-san] Please tell me the episode number: \n')
    addCustomCardsEpisode(title, episode, status)

def menuClassic():
    print("\n[Animu-san] ARA ARA What I can do for you today, Kanan?")
    print(" [D]ownload")
    print(" [U]pdate spreedsheet")
    print(" [1]Add series to Trello")
    print(" [2]Add episodes to Trello")
    print(" [3]Add epissode to Trello")
    print(" [Q]uit\n")

    request = input()

    if request == 'd':
        isThatAMotherFuckingJojoReference('download')
        initDownload()
    elif request == 'u':
        isThatAMotherFuckingJojoReference('update my spreadsheet')
        updateSpreedsheet()
    elif request == '1':
        isThatAMotherFuckingJojoReference('add a series to Trello')
        addSeries()
    elif request == '2':
        isThatAMotherFuckingJojoReference('add episodes to Trello')
        addEpisodes()
    elif request == '3':
        isThatAMotherFuckingJojoReference('add an episode to Trello')
        addEpisode()
    elif request == 'q':
        print("\n        ------------------------------------------------\n"
              "        |                - Bye bye, Kanan-chan! -        |\n"
              "        ------------------------------------------------")
        quit()
    else:
        pass


def menuModern():
    request = input("\n[Animu-san] ARA ARA What I can do for you today, Kanan?\n"
                    "[Kanan-chan] ")

    if 'can you' in request.lower() or 'i want to' in request.lower():
        if 'download' in request.lower():
            isThatAMotherFuckingJojoReference('download')
            initDownload()
        elif 'update' in request.lower():
            isThatAMotherFuckingJojoReference('update my spreadsheet')
            updateSpreedsheet()
        elif 'series to trello' in request.lower():
            isThatAMotherFuckingJojoReference('add a series to Trello')
            addSeries()
        elif 'episodes to trello' in request.lower():
            isThatAMotherFuckingJojoReference('add episodes to Trello')
            addEpisodes()
        elif 'episode to trello' in request.lower():
            isThatAMotherFuckingJojoReference('add an episode to Trello')
            addEpisode()
        else:
            print('[Animu-san] Ara ara, you didn\'t say please...')
    elif 'thank you!' in request.lower() or 'nothing' in request.lower():
        print("\n        ------------------------------------------------\n"
              "        |        - You're welcome! Kanan-chan! -        |\n"
              "        ------------------------------------------------")
        quit()
    else:
        print('[Animu-san] Ara ara Kanan-chan I didn\'t understand. Could you repeat?')
    return True

print("        ------------------------------------------------\n"
      "        | - Welcome Kanan-chan! to ANIMU-SAN v.1.0.1 - |\n"
      "        ------------------------------------------------")

config = configparser.ConfigParser()

if os.path.exists(os.getcwd() + '\\config.ini'):
    config.read('config.ini')
else:
    input('The config file is missing!\n')
    quit()

# Menu
menuType = config.get('MenuType', 'menu')

if menuType == 'classic':
    while True:
        menuClassic()
elif menuType == 'modern':
    while True:
        menuModern()
else:
    print("[Animu-san] Ara ara, I don't know that kind of menu...")
