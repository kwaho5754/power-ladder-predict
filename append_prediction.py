import os
import json
import gspread
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

def append_to_sheet(round_num, time_str, 좌삼짝, 우삼홀, 좌사홀, 우사짝):
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SPREADSHEET_ID = '1SyxM-7xx9miEdbYYxhp69YP9tRLHRA4BQpNOr1O9Q-o'
    RANGE_NAME = '시트1!A1'

    # 환경 변수에서 JSON 문자열을 가져와 파싱
    credentials_info = json.loads(os.environ["GOOGLE_APPLICATION_CREDENTIALS_CONTENT"])
    creds = Credentials.from_service_account_info(credentials_info, scopes=SCOPES)

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

    print("✅ Google Sheet 저장 완료:", result)
