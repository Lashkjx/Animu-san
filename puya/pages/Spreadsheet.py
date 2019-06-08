import gspread as gs
from oauth2client.service_account import ServiceAccountCredentials as sac


# Variables.
scope = ['https://www.googleapis.com/auth/drive']
cred = sac.from_json_keyfile_name('C:/Users/Kanan Lashkjx/.oauth2/my_credential.json', scope)
client = gs.authorize(cred)

# Google sheet file.
sheet = client.open('Animu-san').sheet1

def animeEntriesGS():
    data = True
    animeEntries = []
    i = 2
    while data:
        if sheet.cell(i, 2).value == '':
            data = False
        else:
            animeEntries.append(sheet.cell(i, 2).value)
        i += 1
    return animeEntries

def animeStopGS():
    return sheet.cell(2, 2).value

def getLastEntry():
    return sheet.cell(3,1).value

def setLastEntry(entry):
    sheet.update_cell(3,1,entry)

def getAnimeData(title):
    data = True
    animeData = []
    i = 2
    while data:
        if sheet.cell(i, 2).value == title:
            for j in range(3,6):
                animeData.append(sheet.cell(i, j).value)
            return animeData
            break
        elif(sheet.cell(i,2).value == ''):
            data = False
        i += 1








