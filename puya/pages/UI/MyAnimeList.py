from googlesearch import search
from bs4 import BeautifulSoup
import requests
from resources.CSV.CSV import *


def searchTitle(title, is_seasonal, status):
    for result in search(title + " anime mal", tld="com", num=1, stop=1, pause=0):
        break
    req = requests.get(result)
    soup = BeautifulSoup(req.content, 'html.parser')
    title = soup.select('h1')[0].text.strip()
    duration_mal = soup.find(text='Duration:',
                             attrs={'class': 'spaceit_pad', 'class': 'dark_text'}).next_sibling.strip()
    type = soup.find(text='Type:', attrs={'class': 'dark_text'}).find_next_sibling().get_text()
    duration = duration_mal[:duration_mal.find('.')] + "."
    newEntry = [title, type, duration, is_seasonal.upper(), status]
    add_entry_csv("Anime register", newEntry)
    req.cookies.clear()

show_csv_content("Anime register")

