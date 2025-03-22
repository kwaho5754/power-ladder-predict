import requests

# 1. API에서 데이터 가져오기
url = "https://ntry.com/data/json/games/power_ladder/recent_result.json"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

# 2. 데이터 확인
if response.status_code == 200:
    data = response.json()
    print("✅ 데이터 수집 성공!")

    # 3. 예측을 위한 점수 계산
    predictions = {"좌삼짝": 0, "우삼홀": 0, "좌사홀": 0, "우사짝": 0}

    for game in data[:10]:  # 최근 10개 회차를 기준으로 분석
        start = game["start_point"]
        line = int(game["line_count"])  # 문자열 → 정수 변환
        odd_even = game["odd_even"]

        if start == "LEFT" and line == 3 and odd_even == "ODD":
            predictions["좌삼짝"] += 1
        elif start == "RIGHT" and line == 3 and odd_even == "EVEN":
            predictions["우삼홀"] += 1
        elif start == "LEFT" and line == 4 and odd_even == "EVEN":
            predictions["좌사홀"] += 1
        elif start == "RIGHT" and line == 4 and odd_even == "ODD":
            predictions["우사짝"] += 1

    # 4. 점수가 높은 순으로 정렬하여 상위 3개 예측
    sorted_predictions = sorted(predictions.items(), key=lambda x: x[1], reverse=True)

    print("\n📌 예측 결과 (1~3위):")
    for i, (name, score) in enumerate(sorted_predictions[:3], 1):
        print(f"{i}위: {name} ({score}회)")

else:
    print("⚠️ 데이터를 가져오지 못했습니다.", response.status_code)
