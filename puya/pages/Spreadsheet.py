import gspread as gs
from oauth2client.service_account import ServiceAccountCredentials as sac

# Variables.
scope = ['https://www.googleapis.com/auth/drive']
cred = sac.from_json_keyfile_name('C:/Users/Kanan Lashkjx/.oauth2/my_credential.json', scope)
client = gs.authorize(cred)


def initializeAnimuSan():
    sheet = client.open('Animu-san').sheet1
    return sheet

def initializeAnimuTan():
    sheet = client.open('Animu-san').get_worksheet(1)
    return sheet

def initializeAnimuChan():
    sheet = client.open('Anime 2019').sheet1
    return sheet

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

def getAnimeData(sheet, title, isCustom):
    data = True
    animeData = []
    i = 2
    if isCustom:
        while data:
            if sheet.cell(i, 1).value == title:
                for j in range(2, 4):
                    animeData.append(sheet.cell(i, j).value)
                return animeData
                break
            elif (sheet.cell(i, 2).value == ''):
                data = False
            i += 1
    else:
        while data:
            if sheet.cell(i, 2).value == title:
                for j in range(3,6):
                    animeData.append(sheet.cell(i, j).value)
                return animeData
                break
            elif(sheet.cell(i,2).value == ''):
                data = False
            i += 1



def addEntry(sheet, entryData):
    for entry in range (0, len(entryData)):
        emptyRow = sheet.cell(2, 12).value
        for data in range (0, len(entryData[0])):
            sheet.update_cell(emptyRow, data + 1, str(entryData[entry][data]))
    input("\n       - Thank you! For using me Kanan-chan! -")







