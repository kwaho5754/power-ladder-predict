import json
from collections import Counter

# 임의로 만든 예시 데이터: 실제로는 웹에서 수집한 결과를 여기에 넣으면 됩니다.
recent_patterns = [
    '좌삼짝-우삼홀-좌사홀-우사짝',
    '우삼홀-좌삼짝-우사짝-좌사홀',
    '좌사홀-우삼홀-좌삼짝-우사짝',
    '우사짝-좌사홀-우삼홀-좌삼짝',
    '좌삼짝-좌삼짝-우삼홀-우사짝',
    '좌삼짝-우삼홀-좌사홀-우사짝',
]

# 각 항목별로 쪼개서 분리
slots = [[], [], [], []]  # 0: 첫 번째, 1: 두 번째, ...

for pattern in recent_patterns:
    parts = pattern.split('-')
    for i in range(4):
        slots[i].append(parts[i])

# 각 슬롯별 최빈값 분석
top_1 = Counter(slots[0]).most_common(1)[0][0]
top_2 = Counter(slots[1]).most_common(1)[0][0]
top_3 = Counter(slots[2]).most_common(1)[0][0]
# top_4 = Counter(slots[3]).most_common(1)[0][0]  # 필요 없으면 생략

# ✅ 예측 결과 출력
print("✅ 예측 결과:")
print(f"1위: {top_1}")
print(f"2위: {top_2}")
print(f"3위: {top_3}")

# 💾 최신 결과 저장 (웹에서 확인용)
latest_result = {
    "result": f"1위: {top_1}, 2위: {top_2}, 3위: {top_3}"
}

with open("latest_result.json", "w", encoding="utf-8") as f:
    json.dump(latest_result, f, ensure_ascii=False)
