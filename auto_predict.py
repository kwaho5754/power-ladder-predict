import os
import json
import requests
from datetime import datetime

# 예측 API 주소
url = "https://power-ladder-predict.onrender.com/predict"

# 보낼 데이터 구성
payload = {
    "round": "2025-03-24-01",
    "time": "01:00",
    "좌삼짝": "짝",
    "우삼홀": "홀",
    "좌사홀": "홀",
    "우사짝": "짝"
}

# 예측 요청
response = requests.post(url, json=payload)

# JSON 결과에서 'result'만 추출
try:
    result = response.json()["result"]
    print("✅ 예측 결과:", result)
except Exception as e:
    print("❌ 예측 API에서 JSON 응답을 받지 못했습니다.")
    print("응답 내용:", response.text)
    exit(1)

# ▶ Google Sheets 연동
import gspread
from google.oauth2.service_account import Credentials

def append_to_sheet(round_num, time_str, 좌삼짝, 우삼홀, 좌사홀, 우사짝):
    credentials_json = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS_CONTENT")
    if not credentials_json:
        raise ValueError("GOOGLE_APPLICATION_CREDENTIALS_CONTENT is not set")

    info = json.loads(credentials_json)

    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    credentials = Credentials.from_service_account_info(info, scopes=scopes)
    gc = gspread.authorize(credentials)

    spreadsheet_id = "1SyxM-7xx9miEdbYYxhp69YP9tRLHRA4BQpNOr1O9Q-o"
    sheet = gc.open_by_key(spreadsheet_id).worksheet("예측결과")  # ← 시트 이름 주의!

    values = [[round_num, time_str, 좌삼짝, 우삼홀, 좌사홀, 우사짝]]
    sheet.append_rows(values, value_input_option="RAW")
    print("📌 예측 결과가 Google Sheets에 저장되었습니다.")

# ▶ 시트에 저장 실행
append_to_sheet(
    payload["round"],
    payload["time"],
    payload["좌삼짝"],
    payload["우삼홀"],
    payload["좌사홀"],
    payload["우사짝"]
)
