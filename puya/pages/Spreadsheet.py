import gspread as gs
from oauth2client.service_account import ServiceAccountCredentials as sac


# Variables.
scope = ['https://www.googleapis.com/auth/drive']
cred = sac.from_json_keyfile_name('my_credential.json', scope)
client = gs.authorize(cred)

# Google sheet file.
sheet = client.open('Animu-san').sheet1





