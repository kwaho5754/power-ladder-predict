import os
import json
import gspread
from google.oauth2.service_account import Credentials

def append_to_sheet(round_num, time_str, 좌삼짝, 우삼홀, 좌사홀, 우사짝):
    # 구글 시트 API 인증 범위
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    # 환경변수에서 서비스 계정 JSON을 읽어오기
    service_account_info = json.loads(os.environ['GOOGLE_APPLICATION_CREDENTIALS_JSON'])
    creds = Credentials.from_service_account_info(service_account_info, scopes=SCOPES)

    # gspread 클라이언트 인증
    gc = gspread.authorize(creds)

    # ✅ 실제 Google 시트 ID (링크에서 따온 값)
    SPREADSHEET_ID = '1SyxM-7xx9miEdbYYxhp69YP9tRLHRA4BQpNOr1O9Q-o'

    # ✅ 시트 탭 이름 → 한글로 '시트1' 사용
    worksheet = gc.open_by_key(SPREADSHEET_ID).worksheet("시트1")

    # 추가할 데이터 행
    new_row = [round_num, time_str, 좌삼짝, 우삼홀, 좌사홀, 우사짝]

    # 시트에 추가
    worksheet.append_row(new_row, value_input_option='RAW')
