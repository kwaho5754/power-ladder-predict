import os
import json
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# ► 예측 API 요청
url = "https://power-ladder-predict.onrender.com/predict"
response = requests.post(url, json={})  # 반드시 POST 요청

try:
    result = response.json()  # JSON 파싱 시도
except ValueError:
    print("❌ 예측 API에서 JSON 응답을 받지 못했습니다.")
    print("응답 내용:", response.text)
    exit(1)

# ► Google Sheets 인증
json_content = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS_CONTENT')
credentials_dict = json.loads(json_content)

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials_dict, scope)
client = gspread.authorize(creds)

# ► 시트 열기
spreadsheet = client.open("PowerLadderPrediction")  # 구글 시트 문서 이름
sheet = spreadsheet.worksheet("예측결과")            # 시트 탭 이름

# ► 시간 정보
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ► 예측 결과 Google Sheets에 추가
sheet.append_row([
    "",               # 회차 비워두기 (또는 계산 가능)
    now,
    result["좌삼짝"],
    result["우삼홀"],
    result["좌사홀"],
    result["우사짝"]
])

print("✅ 예측 결과가 성공적으로 시트에 저장되었습니다.")
