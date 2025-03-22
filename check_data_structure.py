import requests
import json

# API에서 데이터 가져오기
url = "https://ntry.com/data/json/games/power_ladder/recent_result.json"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

# 데이터 확인
if response.status_code == 200:
    data = response.json()
    print("✅ 데이터 수집 성공!\n")

    # JSON 데이터의 실제 구조를 보기 쉽게 출력
    print("📌 최근 5개 회차 데이터 예제:")
    print(json.dumps(data[:5], indent=4, ensure_ascii=False))

else:
    print("⚠️ 데이터를 가져오지 못했습니다.", response.status_code)
