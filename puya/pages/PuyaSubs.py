from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from resources.Notifications import *
import os
import time
import sys

def puya(driver, pattern, stop):
    animeArticle = driver.find_elements_by_css_selector("article")
    for anime in animeArticle:
        title = anime.find_element_by_css_selector("h2")
        titlePush = title.text
        if title.text.startswith(pattern):
            match = True
            download = anime.find_elements_by_css_selector("p")
            for option in download:
                if '720p' in option.text:
                    downloadButton = option.find_element_by_css_selector("a:first-child")
                    downloadUrl = downloadButton.get_attribute('href')
                    driver.get(downloadUrl)
                    break
            refresh = True
            while refresh:
                try:
                    resolutionTitle = driver.find_element_by_css_selector("h3:nth-child(1)")
                    torrentButton = driver.find_element_by_css_selector(".panel-footer a:nth-child(2)")
                    refresh = False
                except Exception:
                    driver.refresh()
                    myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h3:nth-child(1)')))
                    resolutionTitle = driver.find_element_by_css_selector("h3:nth-child(1)")
                    torrentButton = driver.find_element_by_css_selector(".panel-footer a:nth-child(2)")
                    refresh = True
            if '[720p]' in resolutionTitle.text:
                os.startfile(torrentButton.get_attribute('href'))
                pushNotification(titlePush)
                driver.get('http://www.puya.moe')
            else:
                print('Wrong resolution')
            return driver
        elif title.text == stop:
            sadNotification = "Sorry senpai, no match today for: " + pattern
            # pushSadNotification(sadNotification)
            print(sadNotification)
            return driver
            break






