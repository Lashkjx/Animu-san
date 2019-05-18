from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import sys

def puya(driver, pattern, stop):
    match = False
    option = None
    animeArticle = driver.find_elements_by_css_selector("article")
    for anime in animeArticle:
        title = anime.find_element_by_css_selector("h2")
        download = anime.find_elements_by_css_selector("div[style]")
        for option in download:
            if '720p' in option.text:
                downloadButton = option.find_element_by_css_selector("a:first-child")
        if title.text.startswith(pattern):
            match = True
            downloadUrl = downloadButton.get_attribute('href')
            driver.get(downloadUrl)
            refresh = True
            while refresh:
                try:
                    resolutionTitle = driver.find_element_by_css_selector("h3:nth-child(1)")
                    torrentButton = driver.find_element_by_css_selector("a.btn.btn-default:nth-child(1)")
                    refresh = False
                except Exception:
                    driver.refresh()
                    myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h3:nth-child(1)')))
                    resolutionTitle = driver.find_element_by_css_selector("h3:nth-child(1)")
                    torrentButton = driver.find_element_by_css_selector("a.btn.btn-default:nth-child(1)")
                    refresh = True
            if '[720p]' in resolutionTitle.text:
                torrentButton.click()
                driver.get('http://www.puya.si')
            else:
                print('Wrong resolution')
            return driver
        elif title.text == stop:
            print("Sorry senpai, no match today")
            return driver
            break






