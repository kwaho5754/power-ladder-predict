
import json
from collections import Counter
import pandas as pd
from scrape_latest_result import scrape_latest_result

# 🔹 CSV 파일에서 과거 데이터 불러오기
df = pd.read_csv("powerladder_data.csv")

# 🔹 각 행을 하나의 조합 문자열로 변환
df["조합"] = df[["좌삼짝", "우삼홀", "좌사홀", "우사짝"]].agg("-".join, axis=1)

# 🔹 조합별 빈도수 세기
counter = Counter(df["조합"])

# 🔹 상위 3개 조합 가져오기
top_3 = counter.most_common(3)

# 🔹 조합 문자열 분해하여 1위, 2위, 3위로 저장
top_predictions = []
for rank, (combo, _) in enumerate(top_3, start=1):
    parts = combo.split("-")
    if parts:
        top_predictions.append(parts[0])
    else:
        top_predictions.append("")

# 🔹 최신 회차 정보 불러오기
latest_round_number = scrape_latest_result()

# 🔹 예측 결과 콘솔 출력
print("✅ 예측 실행 완료")
print(f"🕓 현재 회차: {latest_round_number}")
print("📊 예측 결과:")
print(f"1위: {top_predictions[0]}")
print(f"2위: {top_predictions[1]}")
print(f"3위: {top_predictions[2]}")

# 🔹 JSON 저장 (Flask /latest에서 읽어감)
result = {
    "round": latest_round_number,
    "result": {
        "1위": top_predictions[0],
        "2위": top_predictions[1],
        "3위": top_predictions[2]
    }
}

with open("latest_result.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False)
