import os
import json
import gspread
from google.oauth2.service_account import Credentials

# 환경변수에서 JSON 문서 열 가져오기
json_content = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS_CONTENT")
if json_content is None:
    raise ValueError("GOOGLE_APPLICATION_CREDENTIALS_CONTENT is not set")

# service_account.json 파일로 저장
with open("service_account.json", "w") as f:
    f.write(json_content)

# 인증 설정
scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
creds = Credentials.from_service_account_file("service_account.json", scopes=scope)
gc = gspread.authorize(creds)

# 구글 시트 열기
sheet = gc.open("PowerLadderPrediction").worksheet("Sheet1")

# 시트에 추가하는 함수 정의
def append_to_sheet(round_num, time_str, 좌삼짝, 우삼홀, 좌사홀, 우사짝):
    row = [round_num, time_str, 좌삼짝, 우삼홀, 좌사홀, 우사짝]
    sheet.append_row(row)
    print("✅ 구글 시트에 추가 완료:", row)

# 테스트용 실행 코드
def run():
    append_to_sheet("2025-03-22-01", "00:00", "짝", "홀", "짝", "홀")

if __name__ == "__main__":
    run()
