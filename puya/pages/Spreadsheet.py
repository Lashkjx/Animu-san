import gspread as gs
from oauth2client.service_account import ServiceAccountCredentials as sac


# Variables.
scope = ['https://www.googleapis.com/auth/drive']
cred = sac.from_json_keyfile_name('pages/my_credential.json', scope)
client = gs.authorize(cred)

# Google sheet file.
sheet = client.open('Animu-san').sheet1

def animeEntriesGS():
    data = True
    animeEntries = []
    i = 2
    while data:
        if sheet.cell(i, 1).value == '':
            data = False
        else:
            animeEntries.append(sheet.cell(i, 1).value)
        i += 1
    return animeEntries

def animeStopGS():
    return sheet.cell(2, 2).value

def getAnimeTime():
    return sheet.cell(3,2).value

def setAnimeTime(time):
    sheet.update_cell(3,2,time)






