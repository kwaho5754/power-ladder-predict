import requests
from bs4 import BeautifulSoup

# 1. 사이트 접속
url = "https://ntry.com/scores/power_ladder/main.php"
headers = {"User-Agent": "Mozilla/5.0"}  # 사이트 차단 방지용
response = requests.get(url, headers=headers)

# 2. 응답 상태 코드 출력
print(f"응답 상태 코드: {response.status_code}")

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    # 3. HTML 미리보기 (앞부분 일부 출력)
    print("HTML 일부 미리보기:")
    print(html[:500])  # 앞부분 500자 출력

else:
    print("페이지를 가져오지 못했습니다.")
