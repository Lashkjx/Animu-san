import feedparser
import os

def puyaRSS(anime, stop):
    PuyaSubs = feedparser.parse("https://nyaa.si/?page=rss&u=puyero")
    for entry in PuyaSubs.entries:
        if entry.title != stop:
            if (anime in entry.title) & ('720p' in entry.title):
                magnetPrefix = "magnet:?xt=urn:btih:"
                print("Ara ara, I found a little gift for you: " + entry.title)
                os.startfile(magnetPrefix + entry.nyaa_infohash)
                break
        else:
            sadNotification = "Sorry Kanan-chan, no match today for: " + anime
            print(sadNotification)
            break
    return PuyaSubs.entries[0].title
