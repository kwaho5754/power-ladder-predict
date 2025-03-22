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

    # 📌 최근 5개 회차의 start_point, line_count, odd_even 값 확인
    print("📌 최근 5개 회차 데이터 값 확인:")
    for game in data[:5]:  # 최근 5개 회차만 출력
        print(f"회차: {game['date_round']}, 시작점: {game['start_point']}, 줄 수: {game['line_count']}, 홀짝: {game['odd_even']}")

else:
    print("⚠️ 데이터를 가져오지 못했습니다.", response.status_code)
