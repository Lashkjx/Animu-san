import feedparser
import os

def puyaRSS(anime, stop):
    PuyaSubs = feedparser.parse("https://nyaa.si/?page=rss&u=puyero")
    print(stop)
    for entry in PuyaSubs.entries:
        if entry.published > stop:
            if (anime in entry.title) & ('720p' in entry.title):
                magnetPrefix = "magnet:?xt=urn:btih:"
                os.startfile(magnetPrefix + entry.nyaa_infohash)
                
    sadNotification = "Sorry senpai, no match today for: " + anime
    print(sadNotification)








