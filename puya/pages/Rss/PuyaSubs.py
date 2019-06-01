import feedparser
import os

def puyaRSS(anime, stop):
    PuyaSubs = feedparser.parse("https://nyaa.si/?page=rss&u=puyero")
    for entry in PuyaSubs.entries:
        if entry.title != stop:
            if (anime in entry.title) & ('720p' in entry.title):
                magnetPrefix = "magnet:?xt=urn:btih:"
                os.startfile(magnetPrefix + entry.nyaa_infohash)
                break
        else:
            sadNotification = "Sorry senpai, no match today for: " + anime
            print(sadNotification)
            break
    return PuyaSubs.entries[0].title
