import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def append_to_sheet(round_num, time_str, 좌삼짝, 우삼홀, 좌사홀, 우사짝):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    # Render 환경변수에서 JSON을 문자열로 가져옴
    creds_json = os.getenv("GOOGLE_APPLICATION_CREDENTIALS_CONTENT")
    if not creds_json:
        raise ValueError("GOOGLE_APPLICATION_CREDENTIALS_CONTENT is not set")

    creds_dict = json.loads(creds_json)
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    gc = gspread.authorize(creds)

    # ⬇ 여기 시트 ID와 탭 이름을 정확히 설정하세요! (Sheet1로 변경)
    SPREADSHEET_ID = "1SyxM-7xx9miEdbYYxhp69YP9tRLHRA4BQpNOr1O9Q-o"
   sheet = gc.open("PowerLadderprediction").worksheet("sheet1") 

    values = [round_num, time_str, 좌삼짝, 우삼홀, 좌사홀, 우사짝]
    sheet.append_row(values)
