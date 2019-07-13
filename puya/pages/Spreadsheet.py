import gspread as gs
from oauth2client.service_account import ServiceAccountCredentials as sac
from UI.MyAnimeList import *

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

def animeEntriesGS(sheet):
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

def getLastEntry(sheet):
    return sheet.cell(3,1).value

def setLastEntry(sheet, entry):
    sheet.update_cell(3,1,entry)

def getAnimeDataList(sheet, title, isCustom):
    data = True
    animeList = []
    animeDataList = []
    i = 2
    while data:
        if title in sheet.cell(i, 1).value:
            animeList = [sheet.cell(i, 1).value, i]
            animeDataList.append(animeList)
        elif sheet.cell(i, 1).value == '':
            if len(animeDataList) == 0:
                title = input("\n[Animu-san] Ara ara, I didn\'t understand. Can you repeat it?\n[Kanna-chan] ")
                i = 2
            else:
                data = False
        i += 1
    if len(animeDataList) != 1:
        for j in range(0,len(animeDataList)):
            print("[" + str(j) + "] " + (animeDataList[j])[0])
        try:
            index = input('\n[Animu-san] Ara ara, which of those you\'re refering to?\n[Kanna-chan] ')
            animeDataList[int(index)]
        except IndexError:
            print('[Animu-san] Ara ara, that didn\'t exist! ')
        getAnimu(sheet, (animeDataList[int(index)])[1], isCustom)
    elif len(animeDataList) == 1:
        getAnimu(sheet, (animeDataList[0])[1], isCustom)
    else:
        print("[Animu-san] Ara ara, I didn\'t understand. Can you repeat it?\n[Kanna-chan] ")

def getAnimu(sheet, title, isCustom):
    data = True
    animeData = []
    i = 2
    if isCustom:
        for j in range(1, 6):
            animeData.append(sheet.cell(title, j).value)
    else:
        if title in sheet.cell(i, 2).value:
            for j in range(3,6):
                animeData.append(sheet.cell(title, j).value)
    print(animeData)

def getAnimeData(sheet, title, isCustom):
    data = True
    animeData = []
    i = 2
    if isCustom:
        while data:
            if title in sheet.cell(i, 1).value:
                for j in range(1, 6):
                    animeData.append(sheet.cell(i, j).value)
                return animeData

                break
            elif (sheet.cell(i, 1).value == ''):
                data = False
            i += 1
    else:
        while data:
            if title in sheet.cell(i, 2).value:
                for j in range(3,6):
                    animeData.append(sheet.cell(i, j).value)
                return animeData
                break
            elif(sheet.cell(i,2).value == ''):
                data = False
            i += 1
    print("[Animu-san] Ara ara, I didn\'t understand. Can you repeat it?")


def addEntry(sheet, entryData):
    for entry in range (0, len(entryData)):
        emptyRow = sheet.cell(2, 12).value
        for data in range (0, len(entryData[0])):
            sheet.update_cell(emptyRow, data + 1, str(entryData[entry][data]))
    input("\n[Animu-san] Ara ara, I updated your spreadsheet Kanan-chan!")
