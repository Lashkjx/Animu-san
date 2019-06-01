import feedparser
import os

PuyaSubs = feedparser.parse("https://nyaa.si/?page=rss&u=puyero")
entry = PuyaSubs.entries[2]

print(entry.nyaa_infohash)
magnetPrefix = "magnet:?xt=urn:btih:"
os.startfile(magnetPrefix+entry.nyaa_infohash)
