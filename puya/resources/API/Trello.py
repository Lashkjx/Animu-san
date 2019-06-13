import requests
import json
import os
import configparser
from pages.Spreadsheet import *


def getCredentials():
    if os.path.exists(os.getcwd() + '\\Credentials.ini'):
        cred = configparser.ConfigParser()
        cred.read('Credentials.ini')
        key = cred.get('Credentials', 'key')
        token = cred.get('Credentials', 'token')
        return [key, token]
    else:
        input('The credential file is missing!\n')
        quit()

def addNewCard(key, token, title):
    task = {"idList": "5cf41baca2d0f13ae6397728", "name": title, "desc": "A litle gift from Animu-san to you Kanan-chan...",
            "idLabels":("5cc3877691d0c2ddc511b707", "5cc3877691d0c2ddc511b70a")}
    resp = requests.post('https://api.trello.com/1/cards/?key={}&token={}'.format(key, token), json=task)
    if resp.status_code != 200:
        print('GET /tasks/ {}'.format(resp.status_code))
        return None
    else:
        shortLink = resp.json()["shortLink"]
        return shortLink

def addCustomFields(shortLink, key, token, episode, time, type, status, seasonal):
    # [Number] Episode:
    task = {"value": {"number": episode}}
    customField = '5cfc00571732b354fd81856a'
    resp = requests.put ('https://api.trello.com/1/cards/{}/customField/{}/item/?key={}&token={}'
                         .format(shortLink, customField, key, token), json=task)

    if resp.status_code != 200:
        print('[Error] Episode error: {}'.format(resp.status_code))

    # [Number] Time:
    task = {"value": {"text": time}}
    customField = '5cfd9a2b0b964230a45681d6'
    resp = requests.put ('https://api.trello.com/1/cards/{}/customField/{}/item/?key={}&token={}'
                         .format(shortLink, customField, key, token), json=task)

    if resp.status_code != 200:
        print('[Error] Time error: {}'.format(resp.status_code))

    # [Text] Type:
    task = {"value": {"text": type}}
    customField = '5cfc17ea5fa7063f7b1abae8'
    resp = requests.put ('https://api.trello.com/1/cards/{}/customField/{}/item/?key={}&token={}'
                         .format(shortLink, customField, key, token), json=task)

    if resp.status_code != 200:
        print('[Error] Type error: {}'.format(resp.status_code))

    # [Text] Status:
    task = {"value": {"text": status}}
    customField = '5cfc17ceb3d87c45523dc9a7'
    resp = requests.put ('https://api.trello.com/1/cards/{}/customField/{}/item/?key={}&token={}'
                         .format(shortLink, customField, key, token), json=task)

    if resp.status_code != 200:
        print('[Error] Status error: {}'.format(resp.status_code))

    # [Checkbox] Seasonal:
    task = {"value": {"checked": seasonal}}
    customField = '5cfc00e164a4975195f74fc4'
    resp = requests.put ('https://api.trello.com/1/cards/{}/customField/{}/item/?key={}&token={}'
                         .format(shortLink, customField, key, token), json=task)

    if resp.status_code != 200:
        print('[Error] Seasonal error: {}'.format(resp.status_code))
    else:
        print("Finished!")

def getCards(key, token):
    list = '5cf41ba7fab15d6885a771d7'
    resp = requests.get('https://api.trello.com/1/lists/{}/cards/?customFieldItems=true&key={}&token={}'
                        .format(list, key, token))
    cards = []
    if resp.status_code != 200:
        print('[Error] Card retrival error: {}'.format(resp.status_code))
    else:
        for card in resp.json():
            title = card['name']
            type = 'TV'
            status = 'Watching'
            seasonal = 'NO'
            opening = 'NO'
            ending = 'NO'
            episode = '1'
            overallScore = '5'
            score = '5'
            date = '01/01'
            time = '24 min.'
            for i in range (0, len(card['customFieldItems'])):
                cardResult = card['customFieldItems'][i]
                if '5cfc17ea5fa7063f7b1abae8' in str(cardResult):
                    type = cardResult['value']['text']
                elif '5cfc17ceb3d87c45523dc9a7' in str(cardResult):
                    status = cardResult['value']['text']
                elif '5cfc00571732b354fd81856a' in str(cardResult):
                    episode = cardResult['value']['number']
                elif '5cfc0081e385111a1620a825' in str(cardResult):
                    overallScore  = cardResult['value']['number']
                elif '5cfc006534d0a687623b83aa' in str(cardResult):
                    score = cardResult['value']['number']
                elif '5cfbfeec70352166da99330d' in str(cardResult):
                    date = cardResult['value']['text']
                elif '5cfd9a2b0b964230a45681d6' in str(cardResult):
                    time = cardResult['value']['text']
                elif '5cfc00e164a4975195f74fc4' in str(cardResult):
                    if str(cardResult['value']['checked']) == 'true':
                        seasonal = 'YES'
                elif '5cfc00eaeeea3c5e8fb3dbaf' in str(cardResult):
                    if str(cardResult['value']['checked']) == 'true':
                        opening = 'YES'
                else:
                    if str(cardResult['value']['checked']) == 'true':
                        ending = 'YES'
            anime = [date, title, episode, score, overallScore, type, time, status, seasonal, opening, ending]
            cards.append(anime)
    return cards

def addCustomCardSeries(title, episodes, isSeasonal):
    cred = getCredentials()
    sheet = initializeAnimuTan()
    animeData = getAnimeData(sheet, title, True)
    for ep in range(1,episodes + 1):
        id = addNewCard(cred[0], cred[1], title)
        addCustomFields(id, cred[0], cred[1], str(ep), animeData[0], animeData[1], "Watching", isSeasonal)

def addCustomCardEpisodes(title, first, last, isSeasonal):
    cred = getCredentials()
    sheet = initializeAnimuTan()
    animeData = getAnimeData(sheet, title, True)
    for ep in range(first,last + 1):
        id = addNewCard(cred[0], cred[1], title)
        addCustomFields(id, cred[0], cred[1], str(ep), animeData[0], animeData[1], "Watching", isSeasonal)

def addCustomCardsEpisode(title, episode, isSeasonal):
    cred = getCredentials()
    sheet = initializeAnimuTan()
    animeData = getAnimeData(sheet, title, True)
    id = addNewCard(cred[0], cred[1], title)
    addCustomFields(id, cred[0], cred[1], str(episode), animeData[0], animeData[1], "Watching", isSeasonal)


# addCustomCards('Skirt no Naka wa Kedamono Deshita', 10, 'false')
# addCustomCardsEpisode('Miru Tights', 5, 'false')


# cred = getCredentials()
# cards = getCards(cred[0], cred[1])
# driver = initializeAnimuChan()
# addEntry(driver, cards)
# getCardData(cred[0], cred[1], cards)

