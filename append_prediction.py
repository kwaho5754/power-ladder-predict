from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import os
import json

def append_to_sheet(round_num, time_str, 좌삼짝, 우삼홀, 좌사홀, 우사짝):
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    # 서비스 계정 JSON 환경변수에서 로드
    service_account_info = json.loads(os.environ['GOOGLE_APPLICATION_CREDENTIALS_JSON'])
    creds = Credentials.from_service_account_info(service_account_info, scopes=SCOPES)

    # ✅ 실제 사용 중인 Google 시트 ID
    SPREADSHEET_ID = "1SyxM-7xx9miEdbYYxhp69YP9tRLHRA4BQpNOr1O9Q-o"
    RANGE_NAME = "Sheet1!A1"  # 또는 "시트이름!A1"

    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    values = [[round_num, time_str, 좌삼짝, 우삼홀, 좌사홀, 우사짝]]
    body = {
        'values': values
    }

    result = sheet.values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=RANGE_NAME,
        valueInputOption='RAW',
        insertDataOption='INSERT_ROWS',
        body=body
    ).execute()

    print(f"{result.get('updates').get('updatedCells')} cells appended.")

