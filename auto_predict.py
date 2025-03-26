import os
import json
import requests
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials

# ▶ 현재 시각 기준으로 라운드 및 시간 설정
now = datetime.now()
round_str = now.strftime("%Y-%m-%d-%H")
time_str = now.strftime("%H:%M")

# ▶ 예측에 사용할 입력 데이터 (예: 최근 결과 기반 분석 가능)
payload = {
    "round": round_str,
    "time": time_str,
    "좌삼짝": "짝",
    "우삼홀": "홀",
    "좌사홀": "홀",
    "우사짝": "짝"
}

# ▶ API 요청
url = "https://power-ladder-predict.onrender.com/predict"
response = requests.post(url, json=payload)

try:
    result = response.json()["result"]
    print(f"✅ 예측 결과: {result}")
except Exception as e:
    print("❌ 예측 API에서 JSON 응답을 받지 못했습니다.")
    print("응답 내용:", response.text)
    exit(1)

# ▶ 환경변수에서 서비스 계정 키 정보 읽기
credentials_json = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS_CONTENT")
if not credentials_json:
    raise ValueError("GOOGLE_APPLICATION_CREDENTIALS_CONTENT is not set")

info = json.loads(credentials_json)

# ▶ 인증 및 구글 시트 접속
scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]
credentials = Credentials.from_service_account_info(info, scopes=scopes)
gc = gspread.authorize(credentials)

# ▶ 시트 ID 및 이름
spreadsheet_id = "1SyxM-7xx9miEdbYYxhp69YP9tRLHRA4BQpNOr1O9Q-o"
sheet = gc.open_by_key(spreadsheet_id).worksheet("예측결과")

# ▶ 시트에 추가할 행 구성
values = [[
    payload["round"],
    payload["time"],
    payload["좌삼짝"],
    payload["우삼홀"],
    payload["좌사홀"],
    payload["우사짝"],
    result[0],
    result[1],
    result[2]
]]
sheet.append_rows(values, value_input_option="RAW")
print("📌 예측 결과가 Google Sheets에 저장되었습니다.")
