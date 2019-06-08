import requests
import json


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

# Call to the Watching list
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

# if resp.status_code != 201:
#     path = "c:\\users\\kanan lashkjx\\jason.json"
#     # This means something went wrong.
#     print('GET /tasks/ {}'.format(resp.status_code))
# my_data = json.dumps(resp.json())
# with open(path, 'w') as f:
#     json.dump(my_data + "\n",  f)
# for todo_item in resp.json():
#     print(todo_item, '\n')



# /1/cards/lists/5cf41baca2d0f13ae6397728/
# https://developers.trello.com/reference#cards-2
# "customField":{"type":"checkbox","name":"OP","id":"5cc468d33128436744206048"}
# /1/cards/{id}/idBoard?value={new board ID}&idList={new list ID}
# task = {"idList":"5cf41baca2d0f13ae6397728", "keepFromSource":"all", "name": "KanitaYousoro613", "desc": "Lashkjx","customFieldItems":[{"id":"5cc46bc157011181d2ebdc22","value":{"checked":"true"}}]}
# resp = requests.post('https://api.trello.com/1/cards/?key=400ebd4d957e10315b1737dc60f9dfe5'
#                       '&token=135dc453ffd96de1bb40ecce34767066c6a12d8eb72d14cb567a5c7a35ec6caf', json=task)

task = {"value": { "checked": "true" } }
resp = requests.put ('https://api.trello.com/1/cards/m1ERVtJ1/customField/5cc46bbba062740cc12b1490/item/?key=400ebd4d957e10315b1737dc60f9dfe5'
                     '&token=135dc453ffd96de1bb40ecce34767066c6a12d8eb72d14cb567a5c7a35ec6caf', json=task)

# resp = requests.post('https://todolist.example.com/tasks/', json=task)
if resp.status_code != 200:
    print('GET /tasks/ {}'.format(resp.status_code))
else:
    print('Good Job!')
