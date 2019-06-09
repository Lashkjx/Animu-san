import requests
import json
import os
import configparser


# Call to everything.
# resp = requests.get('https://api.trello.com/1/members/me/boards?key=400ebd4d957e10315b1737dc60f9dfe5'
#                     '&token=135dc453ffd96de1bb40ecce34767066c6a12d8eb72d14cb567a5c7a35ec6caf')

# Call to the board "Anime Board".
# resp = requests.get('https://api.trello.com/1/boards/vD6NfCPz?key=400ebd4d957e10315b1737dc60f9dfe5'
#                     '&token=135dc453ffd96de1bb40ecce34767066c6a12d8eb72d14cb567a5c7a35ec6caf')

# Call to the lists of the board
# resp = requests.get('https://api.trello.com/1/boards/vD6NfCPz/lists/?key=400ebd4d957e10315b1737dc60f9dfe5'
#                     '&token=135dc453ffd96de1bb40ecce34767066c6a12d8eb72d14cb567a5c7a35ec6caf')

# Call to the Tabureto list
# resp = requests.get('https://api.trello.com/1/lists/5cf41baca2d0f13ae6397728/cards/?key=400ebd4d957e10315b1737dc60f9dfe5'
#                     '&token=135dc453ffd96de1bb40ecce34767066c6a12d8eb72d14cb567a5c7a35ec6caf')

# Call to the Watched list
# resp = requests.get('https://api.trello.com/1/lists/5cf41ba7fab15d6885a771d7/cards/?key=400ebd4d957e10315b1737dc60f9dfe5'
#                     '&token=135dc453ffd96de1bb40ecce34767066c6a12d8eb72d14cb567a5c7a35ec6caf')

# Call to the Dropped list
# resp = requests.get('https://api.trello.com/1/lists/5cc3877622aac58e58061205/cards/?key=400ebd4d957e10315b1737dc60f9dfe5'
                    # '&token=135dc453ffd96de1bb40ecce34767066c6a12d8eb72d14cb567a5c7a35ec6caf')

# Call to the custom fields
# resp = requests.get('https://api.trello.com/1/boards/vD6NfCPz/customFields?key=400ebd4d957e10315b1737dc60f9dfe5'
#                     '&token=135dc453ffd96de1bb40ecce34767066c6a12d8eb72d14cb567a5c7a35ec6caf')

# Call cards
# resp = requests.get('https://api.trello.com/1/cards/kHBzTBnr/customFields/?key=400ebd4d957e10315b1737dc60f9dfe5'
#                     '&token=135dc453ffd96de1bb40ecce34767066c6a12d8eb72d14cb567a5c7a35ec6caf')

# Labels
# resp = requests.get('https://api.trello.com/1/boards/vD6NfCPz/labels/?key=400ebd4d957e10315b1737dc60f9dfe5'
#                     '&token=135dc453ffd96de1bb40ecce34767066c6a12d8eb72d14cb567a5c7a35ec6caf')

# if resp.status_code != 201:
#     path = "c:\\users\\kanan lashkjx\\jason.json"
#     # This means something went wrong.
#     print('GET /tasks/ {}'.format(resp.status_code))
# # my_data = json.dumps(resp.json())
# # with open(path, 'w') as f:
# #     json.dump(my_data + "\n",  f)
# for todo_item in resp.json():
#     print(todo_item['shortLink'], '\n')



# /1/cards/lists/5cf41baca2d0f13ae6397728/
# https://developers.trello.com/reference#cards-2
# "customField":{"type":"checkbox","name":"OP","id":"5cc468d33128436744206048"}
# /1/cards/{id}/idBoard?value={new board ID}&idList={new list ID}
# task = {"idList":"5cf41baca2d0f13ae6397728", "name": "Kashikoi Kawaii", "desc": "Hola"}
# resp = requests.post('https://api.trello.com/1/cards/?key=400ebd4d957e10315b1737dc60f9dfe5'
#                       '&token=135dc453ffd96de1bb40ecce34767066c6a12d8eb72d14cb567a5c7a35ec6caf', json=task)

# task = {"value": { "checked": "true" } }
# resp = requests.put ('https://api.trello.com/1/cards/m1ERVtJ1/customField/5cc46bbba062740cc12b1490/item/?key=400ebd4d957e10315b1737dc60f9dfe5'
#                      '&token=135dc453ffd96de1bb40ecce34767066c6a12d8eb72d14cb567a5c7a35ec6caf', json=task)

# resp = requests.post('https://todolist.example.com/tasks/', json=task)
# if resp.status_code != 200:
#     print('GET /tasks/ {}'.format(resp.status_code))
# else:
#     # for todo_item in resp.json():
#     #     print(todo_item, '\n')
#     # print('Good Job!')
#     print('Created card. Short ID: {}'.format(resp.json()["shortLink"]))
#     print('Good Job!')

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
    task = {"value": {"number": time}}
    customField = '5cfc009ada495f2053d781ff'
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
            print('Title:' ,card['name'])
            for i in range (1, len(card['customFieldItems'])):
                cardResult = card['customFieldItems'][i]
                input(cardResult)
                if '5cfc17ea5fa7063f7b1abae8' in str(cardResult):
                    print('Type:', cardResult['value']['text]'])
                elif '5cfc17ceb3d87c45523dc9a7' in str(cardResult):
                    print('Status:',cardResult['value']['text'])
                elif '5cfc00e164a4975195f74fc4' in str(cardResult):
                    print('Seasonal:', cardResult['value']['checked'])
                elif '5cfc009ada495f2053d781ff' in str(cardResult):
                    print('Episode:', cardResult['value']['number'])
                elif '5cfc0081e385111a1620a825' in str(cardResult):
                    print('Overall score:', cardResult['value']['number'])
                elif '5cfc006534d0a687623b83aa' in str(cardResult):
                    print('Score:', cardResult['value']['number'])
                elif '5cfc00571732b354fd81856a' in str(cardResult):
                    print('Episode:', cardResult['value']['number'])
                elif '5cfbfeec70352166da99330d' in str(cardResult):
                    print('Date:', cardResult['value']['text'])
                elif '5cfc00eaeeea3c5e8fb3dbaf' in str(cardResult):
                    print('Opening:', cardResult['value']['checked'])
                elif '5cfc009ada495f2053d781ff' in str(cardResult):
                    print('Time:', cardResult['value']['number'])
                else:
                    print('Ending:', cardResult['value']['checked'])




            print(card['customFieldItems'])
            # title = card['name']
            # shortLink = card['shortLink']
            # cards.append([title, shortLink])
        return cards


def getCardData(key, token, cards):
    for card in cards:
        shortLink = card[1]
        resp = requests.get('https://api.trello.com/1/cards/{}/customFields/?key={}''&token={}'
                            .format(shortLink, key, token))
        print('Name: ', cards[0])
        print(resp.json())

cred = getCredentials()
cards = getCards(cred[0], cred[1])
# getCardData(cred[0], cred[1], cards)

