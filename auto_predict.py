import json
from collections import Counter

# 예시 데이터 (실제에서는 크롤링이나 DB에서 불러오도록 구성 가능)
# 형식: ['좌삼짝-우삼홀-좌사홀-우사짝', ...]
past_patterns = [
    '좌삼짝-우삼홀-좌사홀-우사짝',
    '좌삼짝-우삼홀-좌사홀-우사짝',
    '우삼홀-좌삼짝-우사짝-좌사홀',
    '좌삼짝-우삼홀-좌사홀-우사짝',
    '우삼홀-좌삼짝-우사짝-좌사홀',
    '좌삼짝-우삼홀-좌사홀-우사짝',
    '좌삼짝-우삼홀-좌사홀-우사짝',
]

# 빈도수 분석
pattern_counter = Counter(past_patterns)
top_patterns = pattern_counter.most_common(3)

# 예측 결과 문자열 구성
prediction_result = ""
for idx, (pattern, count) in enumerate(top_patterns, start=1):
    prediction_result += f"{idx}위: {pattern}"
    if idx != len(top_patterns):
        prediction_result += ", "

# 콘솔 출력용
print("✅ 예측 결과:", prediction_result)

# 파일 저장용
result_data = {
    "result": prediction_result
}

with open("latest_result.json", "w", encoding="utf-8") as f:
    json.dump(result_data, f, ensure_ascii=False)
