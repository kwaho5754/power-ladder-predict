import requests
from collections import Counter

# 1. API에서 데이터 가져오기
url = "https://ntry.com/data/json/games/power_ladder/recent_result.json"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("✅ 데이터 수집 성공!")

    # 2. 실제 데이터에서 가장 많이 등장하는 패턴 찾기
    pattern_counter = Counter()

    print("\n🔍 전체 데이터에서 등장하는 패턴 확인:")
    for game in data:  
        start = game["start_point"].strip().upper()  
        line = game["line_count"].strip()  
        odd_even = game["odd_even"].strip().upper()  
        
        pattern = f"{start}, {line}, {odd_even}"
        pattern_counter[pattern] += 1  # 패턴 개수 카운트

    # 3. 가장 많이 등장한 패턴 상위 10개 출력
    print("\n📌 가장 많이 등장한 패턴 (상위 10개):")
    for pattern, count in pattern_counter.most_common(10):
        print(f"{pattern}: {count}회")

else:
    print("⚠️ 데이터를 가져오지 못했습니다.", response.status_code)
