import requests

# 1. API URL 설정
url = "https://ntry.com/data/json/games/power_ladder/recent_result.json"

# 2. 요청 보내기
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

# 3. JSON 데이터 확인
if response.status_code == 200:
    data = response.json()
    print("✅ 데이터 수집 성공!")
    
    # 4. 데이터 예제 출력 (최신 5개만)
    for game in data[:5]:  # 최근 5개 회차 데이터
        print(f"회차: {game['date_round']}, 시작점: {game['start_point']}, 줄 수: {game['line_count']}, 홀짝: {game['odd_even']}")

else:
    print("⚠️ 데이터를 가져오지 못했습니다.", response.status_code)
