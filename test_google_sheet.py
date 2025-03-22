import gspread
from oauth2client.service_account import ServiceAccountCredentials

# 구글 시트 접근을 위한 설정
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("vertical-hook-454512-j7-923cfa34df58.json", scope)  # 파일 이름 수정!
client = gspread.authorize(creds)

# 구글 시트 열기
spreadsheet = client.open("data")  # 구글 시트 이름
worksheet = spreadsheet.sheet1     # 첫 번째 시트 선택

# 테스트로 데이터 한 줄 쓰기
worksheet.append_row(["test_round", "12:00", "짝", "홀", "홀", "짝"])

print("✅ Google Sheet에 한 줄 추가 완료!")
