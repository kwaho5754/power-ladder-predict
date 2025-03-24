import os
import json
import gspread
from google.oauth2.service_account import Credentials

def append_to_sheet(round_num, time_str, 좌삼짝, 우삼홀, 좌사홀, 우사짝):
    credentials_json = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS_CONTENT")
    if not credentials_json:
        raise ValueError("GOOGLE_APPLICATION_CREDENTIALS_CONTENT is not set")

    info = json.loads(credentials_json)

    scopes = ['https://www.googleapis.com/auth/spreadsheets']
    credentials = Credentials.from_service_account_info(info, scopes=scopes)
    gc = gspread.authorize(credentials)

    spreadsheet_id = "1SyxM-7xx9miEdbYYxhp69YP9tRLHRA4BQpNOr1O9Q-o"  # 시트 ID
    sheet = gc.open_by_key(spreadsheet_id).worksheet("예측결과")   # ✅ 수정된 부분

    values = [[round_num, time_str, 좌삼짝, 우삼홀, 좌사홀, 우사짝]]
    sheet.append_rows(values, value_input_option="RAW")
