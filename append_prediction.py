import gspread
from oauth2client.service_account import ServiceAccountCredentials

# 구글 시트 접근 권한 설정
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("vertical-hook-454512-j7-923cfa34df58.json", scope)
client = gspread.authorize(creds)

# 구글 시트 열기
spreadsheet = client.open("data")  # 구글 시트 이름
worksheet = spreadsheet.sheet1      # 첫 번째 시트

# 예측된 데이터 (임시 테스트용)
round = "2025-03-22-01"
time = "00:00"
좌삼짝 = "짝"
우삼홀 = "홀"
좌사홀 = "홀"
우사짝 = "짝"

# 구글 시트에 추가
worksheet.append_row([round, time, 좌삼짝, 우삼홀, 좌사홀, 우사짝])
print("✅ 예측 결과를 구글 시트에 추가 완료!")
