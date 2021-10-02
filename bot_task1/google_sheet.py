from googleapiclient.discovery import build
from google.oauth2 import service_account
from config import GOOGLE_SPREAD_SHEET


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'credentials.json'

credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a spreadsheet.
SPREADSHEET_ID = GOOGLE_SPREAD_SHEET
RANGE_NAME = 'Sheet1'

service = build('sheets', 'v4', credentials=credentials)


def make_sorted_srt_from_list(data):
    languages = ''
    for i in sorted(data['language']):
        if languages == '':
            languages += i
        else:
            languages += ', ' + i
    return languages


def add_to_spread_sheet(data, chat_id, tg_username):
    languages = make_sorted_srt_from_list(data)
    array_ = {'values': [[chat_id, tg_username, data['name'], data['phone_number'], languages]]}
    range_ = 'Sheet1!A2:Z10000'
    request = service.spreadsheets().values().append(spreadsheetId=SPREADSHEET_ID,
                                                     range=range_,
                                                     valueInputOption='USER_ENTERED',
                                                     insertDataOption='INSERT_ROWS',
                                                     body=array_)
    response = request.execute()



