from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

def append_to_sheet(round_num, time_str, 좌삼짝, 우삼홀, 좌사홀, 우사짝):
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SPREADSHEET_ID = '구글 시트 ID 넣기'
    RANGE_NAME = '시트이름!A1'

    creds = Credentials.from_service_account_file('service_account.json', scopes=SCOPES)
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    values = [[round_num, time_str, 좌삼짝, 우삼홀, 좌사홀, 우사짝]]
    body = {'values': values}

    result = sheet.values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=RANGE_NAME,
        valueInputOption='RAW',
        insertDataOption='INSERT_ROWS',
        body=body
    ).execute()
