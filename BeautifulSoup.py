import requests
from bs4 import BeautifulSoup

url = "https://example.com/powerladder_results"  # 실제 URL로 변경

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    print("데이터 수집 성공!")
else:
    print("페이지 로딩 실패:", response.status_code)
