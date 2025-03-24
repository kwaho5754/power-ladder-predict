import os
import json
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# ▶ 예측 API 요청
url = "https://power-ladder-predict.onrender.com/predict"
response = requests.post(url, json={})  # POST 요청 (중요!)
result = response.json()["result"]      # 예: {'좌삼짝': 0.84, '우삼홀': 0.33, '좌사홀': 0.77, '우사짝': 0.25}

# ▶ Google Sheets 인증
json_content = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS_CONTENT')
credentials_dict = json.loads(json_content)

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials_dict, scope)
client = gspread.authorize(creds)

# ▶ 시트 열기
spreadsheet = client.open("PowerLadder")         # ← 구글 시트 문서 이름
sheet = spreadsheet.worksheet("예측결과")         # ← 시트 탭 이름 (예: '예측결과')

# ▶ 시간 정보
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ▶ 예측 결과 Google Sheets에 추가
sheet.append_row([
    "",            # 회차는 생략 (혹은 계산 가능)
    now,
    result["좌삼짝"],
    result["우삼홀"],
    result["좌사홀"],
    result["우사짝"]
])

print("예측 결과가 성공적으로 시트에 저장되었습니다.")
