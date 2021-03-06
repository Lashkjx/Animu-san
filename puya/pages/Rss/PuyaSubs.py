import feedparser
import re
from pages.Spreadsheet import *
from resources.API.Trello import *


def addTrelloCard(title, episode):
    driver = initializeAnimuSan()
    animeData = getAnimeData(driver, title, False)
    cred = getCredentials()
    id = addNewCard(cred[0], cred[1], title)
    addCustomFields(id, cred[0], cred[1], episode, animeData[0], animeData[1], "Watching", "true")


def puyaRSS(anime, stop):
    PuyaSubs = feedparser.parse("https://nyaa.si/?page=rss&u=puyero")
    for entry in PuyaSubs.entries:
        if entry.title != stop:
            if (anime in entry.title) & ('720p' in entry.title):
                magnetPrefix = "magnet:?xt=urn:btih:"
                os.startfile(magnetPrefix + entry.nyaa_infohash)
                pattern = "\d\d"
                reEpisode = re.findall(pattern, entry.title)
                if int(reEpisode[0]) < 10:
                    episode = str(reEpisode[0])[1]
                else:
                    episode = str(reEpisode[0])
                print("[Animu-san] Ara ara, I found a little gift for you: " + anime + " - " + episode)
                addTrelloCard(anime, episode)
                break
        else:
            sadNotification = "[Animu-san] Sorry Kanan-chan, no match today for: " + anime
            print(sadNotification)
            break
    return PuyaSubs.entries[0].title
