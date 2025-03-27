import os
import json
import requests
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials

# ▶ 시간 자동 설정
now = datetime.now()
round_str = now.strftime("%Y-%m-%d-%H")
time_str = now.strftime("%H:%M")

# ▶ API 요청을 위한 데이터 구성
payload = {
    "round": round_str,
    "time": time_str,
    "좌삼짝": "짝",
    "우삼홀": "홀",
    "좌사홀": "홀",
    "우사짝": "짝"
}

# ▶ API 요청
try:
    response = requests.post("https://power-ladder-predict.onrender.com/predict", json=payload)
    result = response.json()["result"]
    print("✅ 예측 결과:", result)
except Exception as e:
    print("❌ 예측 API 오류:", e)
    print("응답 내용:", response.text)
    exit(1)

# ▶ 서비스 계정 키 환경변수 로드
credentials_json = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS_CONTENT")
if not credentials_json:
print("⚠️ 환경변수 GOOGLE_APPLICATION_CREDENTIALS_CONTENT 없음 - 시트 저장은 생략됩니다.")  

info = json.loads(credentials_json)
scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]
credentials = Credentials.from_service_account_info(info, scopes=scopes)
gc = gspread.authorize(credentials)

# ▶ 시트 열기
spreadsheet_id = "1SyxM-7xx9miEdbYYxhp69YP9tRLHRA4BQpNOr1O9Q-o"
sheet = gc.open_by_key(spreadsheet_id).worksheet("예측결과")

# ▶ 시트에 결과 추가
values = [[
    payload["round"],
    payload["time"],
    payload["좌삼짝"],
    payload["우삼홀"],
    payload["좌사홀"],
    payload["우사짝"],
    result.split(",")[0].split(":")[1].strip(),
    result.split(",")[1].split(":")[1].strip(),
    result.split(",")[2].split(":")[1].strip()
]]
sheet.append_rows(values, value_input_option="RAW")
print("📌 Google Sheets에 저장 완료")
