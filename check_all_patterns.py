import requests

# 1. API에서 데이터 가져오기
url = "https://ntry.com/data/json/games/power_ladder/recent_result.json"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("✅ 데이터 수집 성공!")

    # 2. 예측을 위한 점수 계산
    predictions = {"좌삼짝": 0, "우삼홀": 0, "좌사홀": 0, "우사짝": 0}

    print("\n🔍 전체 데이터에서 패턴이 존재하는지 확인:")
    for game in data:  # **전체 데이터 검색**
        start = game["start_point"].strip().upper()  # 공백 제거 및 대문자 변환
        line = game["line_count"].strip()  # 문자열 그대로 비교
        odd_even = game["odd_even"].strip().upper()  # 공백 제거 및 대문자 변환

        if start == "LEFT" and line == "3" and odd_even == "ODD":
            predictions["좌삼짝"] += 1
        elif start == "RIGHT" and line == "3" and odd_even == "EVEN":
            predictions["우삼홀"] += 1
        elif start == "LEFT" and line == "4" and odd_even == "EVEN":
            predictions["좌사홀"] += 1
        elif start == "RIGHT" and line == "4" and odd_even == "ODD":
            predictions["우사짝"] += 1

    # 3. 점수가 높은 순으로 정렬하여 상위 3개 예측
    sorted_predictions = sorted(predictions.items(), key=lambda x: x[1], reverse=True)

    print("\n📌 전체 데이터에서 나온 패턴 개수:")
    for name, score in sorted_predictions:
        print(f"{name}: {score}회")

else:
    print("⚠️ 데이터를 가져오지 못했습니다.", response.status_code)
